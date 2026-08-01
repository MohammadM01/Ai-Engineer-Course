import { useEffect, useRef, useState } from "react";
import "./App.css";
import profile from "./assets/profile.png";
import { SiLeetcode } from "react-icons/si";
import {
  FaMoon,
  FaSun,
  FaTrash,
  FaGithub,
  FaLinkedin,
  FaFilePdf,
  FaUser,
  FaCode,
  FaLaptopCode,
  FaGraduationCap,
  FaAward,
  FaEnvelope,
  FaCopy,
} from "react-icons/fa";

function App() {
  const [theme, setTheme] = useState("light");

  const [chatId, setChatId] = useState("");

  const [question, setQuestion] = useState("");

  const [loading, setLoading] = useState(false);

  const [messages, setMessages] = useState([
    {
      role: "ai",
      text: `Hi, I'm Mohammad's AI assistant.

Ask me anything about:

• About
• Skills
• Projects
• Education
• Experience
• Achievements`,
    },
  ]);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    document.body.className = theme;
  }, [theme]);

  useEffect(() => {
    createChat();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  async function createChat() {
    const response = await fetch("http://127.0.0.1:8000/new-chat");

    const data = await response.json();

    setChatId(data.chat_id);
  }

  async function clearChat() {
    await createChat();

    setMessages([
      {
        role: "ai",
        text: `Hi, I'm Mohammad's AI assistant.

Ask me anything about:

• About
• Skills
• Projects
• Education
• Experience
• Achievements`,
      },
    ]);

    setQuestion("");
  }
  async function sendMessage(customQuestion) {
    const userQuestion = customQuestion || question;

    if (!userQuestion.trim()) return;

    if (loading) return;

    setLoading(true);

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        text: userQuestion,
      },
      {
        role: "ai",
        text: "Thinking...",
      },
    ]);

    setQuestion("");

    const response = await fetch(
      `http://127.0.0.1:8000/chat?chat_id=${chatId}&question=${encodeURIComponent(userQuestion)}`,
    );

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    let answer = "";

    while (true) {
      const { done, value } = await reader.read();

      if (done) break;

      answer += decoder.decode(value);
      answer = answer
        .replace(/\*\*/g, "")
        .replace(/\*/g, "")
        .replace(/#{1,6}\s?/g, "")
        .replace(/`/g, "");
        
      setMessages((prev) => {
        const temp = [...prev];

        temp[temp.length - 1] = {
          ...temp[temp.length - 1],
          text: answer,
        };

        return temp;
      });
    }

    setLoading(false);
  }

  function quickAsk(question) {
    sendMessage(question);
  }

  function copyText(text) {
    navigator.clipboard.writeText(text);
  }

  function toggleTheme() {
    setTheme(theme === "light" ? "dark" : "light");
  }

  return (
    <div className={`app ${theme}`}>
      <div className="portfolio-layout">
        {/* ---------- LEFT SIDEBAR ---------- */}

        <aside className="sidebar">
          <div className="logo">
            <h1>AI Portfolio</h1>

            <p>Mohammad Mulla</p>
          </div>

          <img src={profile} alt="Mohammad" className="profile-photo" />

          <h2 className="name">Mohammad Mulla</h2>

          <p className="role">Software Engineer</p>

          <p className="stack">React • Java • Python • FastAPI • MongoDB</p>

          <div className="socials">
            <a
              href="/Mohammad_Mulla_Resume.pdf"
              target="_blank"
              rel="noreferrer"
              className="resume-btn"
            >
              <FaFilePdf />
            </a>

            <a
              href="https://github.com/MohammadM01"
              target="_blank"
              rel="noreferrer"
              className="github-btn"
            >
              <FaGithub />
            </a>

            <a
              href="https://leetcode.com/u/MohammadM01/"
              target="_blank"
              rel="noreferrer"
              className="leetcode-btn"
            >
              <SiLeetcode />
            </a>

            <a
              href="https://linkedin.com/in/mohammadm01"
              target="_blank"
              rel="noreferrer"
              className="linkedin-btn"
            >
              <FaLinkedin />
            </a>
          </div>

          <div className="theme-buttons">
            <button className="theme-btn" onClick={toggleTheme}>
              {theme === "light" ? <FaMoon /> : <FaSun />}
            </button>

            <button className="clear-btn" onClick={clearChat}>
              <FaTrash />
            </button>
          </div>
        </aside>

        {/* ---------- MAIN ---------- */}

        <main className="main">
          <section className="hero-card">
            <div>
              <h2>Hello 👋</h2>

              <p>
                I'm Mohammad's AI Assistant. Ask me anything about my education,
                skills, projects, achievements or experience.
              </p>
            </div>
          </section>

          <section className="quick-actions">
            <button onClick={() => quickAsk("Tell me about Mohammad")}>
              <FaUser />
              <span>About</span>
            </button>

            <button onClick={() => quickAsk("Tell me about his skills")}>
              <FaCode />
              <span>Skills</span>
            </button>

            <button onClick={() => quickAsk("Tell me about his projects")}>
              <FaLaptopCode />
              <span>Projects</span>
            </button>

            <button onClick={() => quickAsk("Tell me about his education")}>
              <FaGraduationCap />
              <span>Education</span>
            </button>

            <button onClick={() => quickAsk("Tell me about his achievements")}>
              <FaAward />
              <span>Awards</span>
            </button>

            <button onClick={() => quickAsk("How can I contact Mohammad")}>
              <FaEnvelope />
              <span>Contact</span>
            </button>
          </section>

          <section className="messages">
            {messages.map((message, index) => (
              <div key={index} className={`message ${message.role}`}>
                <div className="bubble">
                  <div className="bubble-header">
                    <strong>
                      {message.role === "ai" ? "AI Assistant" : "You"}
                    </strong>

                    {message.role === "ai" &&
                      message.text !== "Thinking..." && (
                        <button
                          className="copy-btn"
                          onClick={() => copyText(message.text)}
                        >
                          <FaCopy />
                        </button>
                      )}
                  </div>

                  <p>{message.text}</p>
                </div>
              </div>
            ))}

            <div ref={messagesEndRef}></div>
          </section>

          <section className="input-area">
            <input
              type="text"
              value={question}
              placeholder="Ask anything about Mohammad..."
              disabled={loading}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  sendMessage();
                }
              }}
            />

            <button onClick={sendMessage} disabled={loading}>
              {loading ? "Thinking..." : "Send"}
            </button>
          </section>
        </main>
      </div>
    </div>
  );
}

export default App;
