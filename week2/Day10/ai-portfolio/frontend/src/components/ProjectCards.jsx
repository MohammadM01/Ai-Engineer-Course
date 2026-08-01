import { FaGithub, FaExternalLinkAlt, FaRocket, FaShieldAlt, FaCoins, FaEye } from "react-icons/fa";

const projectsData = [
  {
    id: "cryptguard",
    name: "CryptGuard",
    icon: <FaShieldAlt style={{ color: "#8b5cf6" }} />,
    tagline: "Privacy-Preserving Threat Detection",
    description: "Privacy-preserving encrypted network traffic threat detection system using Deep Packet Inspection (DPI), TLS fingerprinting (JA3), and ML classification.",
    tech: ["C++", "Python", "DPI", "Machine Learning", "TLS", "JA3"],
    github: "https://github.com/MohammadM01/CryptGuard",
    demo: null,
    badge: "AI & Security",
  },
  {
    id: "chaincred",
    name: "ChainCred",
    icon: <FaCoins style={{ color: "#3b82f6" }} />,
    tagline: "Decentralized Verifiable Credentials",
    description: "Web3 verifiable credential platform built on opBNB and BNB Greenfield for tamper-proof educational and professional certificate issuance.",
    tech: ["React", "Node.js", "MongoDB", "Solidity", "opBNB", "Greenfield"],
    github: "https://github.com/MohammadM01/Chain-Cred-final",
    demo: "https://chaincred-frontend.onrender.com/",
    badge: "Web3 & Blockchain",
  },
  {
    id: "civiceye",
    name: "Civic Eye",
    icon: <FaEye style={{ color: "#10b981" }} />,
    tagline: "Unified Civic Issue Resolution Platform",
    description: "AI-driven public infrastructure issue reporting platform utilizing YOLOv8 computer vision model for automatic pothole and garbage detection.",
    tech: ["React", "Node.js", "Express", "YOLOv8", "Blockchain", "REST APIs"],
    github: "https://github.com/MohammadM01/civic",
    demo: null,
    badge: "Computer Vision",
  },
];

export default function ProjectCards() {
  return (
    <div className="project-cards-wrapper">
      <div className="project-cards-header">
        <FaRocket style={{ color: "#ec4899", marginRight: 8 }} />
        <span>Featured Engineering Projects</span>
      </div>
      <div className="project-cards-grid">
        {projectsData.map((project) => (
          <div key={project.id} className="project-card">
            <div className="project-card-top">
              <div className="project-title-group">
                <span className="project-icon">{project.icon}</span>
                <div>
                  <h4 className="project-name">{project.name}</h4>
                  <p className="project-tagline">{project.tagline}</p>
                </div>
              </div>
              <span className="project-badge">{project.badge}</span>
            </div>

            <p className="project-description">{project.description}</p>

            <div className="project-tech-pills">
              {project.tech.map((t, idx) => (
                <span key={idx} className="tech-pill">
                  {t}
                </span>
              ))}
            </div>

            <div className="project-actions">
              <a
                href={project.github}
                target="_blank"
                rel="noreferrer"
                className="proj-btn proj-github"
              >
                <FaGithub /> GitHub
              </a>
              {project.demo && (
                <a
                  href={project.demo}
                  target="_blank"
                  rel="noreferrer"
                  className="proj-btn proj-demo"
                >
                  <FaExternalLinkAlt /> Live Demo
                </a>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
