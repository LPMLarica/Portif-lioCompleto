import streamlit as st
import plotly.graph_objects as go
import base64
from pathlib import Path

st.set_page_config(
    page_title="Larissa Campos | AI Developer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
def carregar_css(style):
    with open(str(Path(style))) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

carregar_css("static/style.css")

# Sidebar for navigation
st.sidebar.markdown("# Navigation")
page = st.sidebar.radio(
    "Navigation Menu",
    ["Home", "Certificates"],
    label_visibility="collapsed"
)

# Function to create radar chart
def create_skills_radar():
    skills = {
        'Python': 95,
        'AI & ML': 90,
        'JavaScript': 75,
        'Angular': 70,
        'Golang': 65,
        'Frontend (HTML/CSS)': 80,
        'Chatbots': 90,
        'Blender 3D': 60,
        'Git/GitHub': 85,
        'Streamlit': 75
    }
    
    categories = list(skills.keys())
    values = list(skills.values())
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skill Level',
        line=dict(color='#00f0ff', width=2),
        fillcolor='rgba(0, 240, 255, 0.3)',
        hovertemplate='<b>%{theta}</b><br>Level: %{r}%<extra></extra>'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='rgba(0, 240, 255, 0.3)',
                tickfont=dict(color='#00f0ff', size=10)
            ),
            angularaxis=dict(
                gridcolor='rgba(138, 43, 226, 0.3)',
                tickfont=dict(color='#e0e0e0', size=12)
            ),
            bgcolor='rgba(10, 14, 39, 0.5)'
        ),
        showlegend=True,
        title=dict(
            text="Technical Skills Map",
            font=dict(size=20, color='#00f0ff', family='Orbitron')
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0e0'),
        height=600
    )
    
    return fig, skills

# CV Download
def get_cv_download():
    cv_path = Path("documents-images") / "Document 4.pdf"
    if cv_path.exists():
        with open(cv_path, "rb") as file:
            pdf_bytes = file.read()
            b64_pdf = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="CV_Larissa_Campos.pdf" class="download-button">📥 Download Resume (PDF)</a>'
            return href
    return None

def get_cover_download():
    cover_path = Path("documents-images") / "Cover Letter (1).pdf" 
    if cover_path.exists():
        with open(cover_path, "rb") as file:
            pdf_bytes = file.read()
            b64_pdf = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="CoverLetter_Larissa_Campos.pdf" class="download-button">📥 Download Cover Letter (PDF)</a>'
            return href
    return None

if page == "Home":
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            profile_image = Path("documents-images") / "eu.jpg"
            st.image(str(profile_image), width=200)
        except Exception as e:
            st.markdown("""
            <div class='profile-image-container'>
                <div class='profile-circle'>
                    <p class='image-placeholder'>Image not found</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
    
    with col2:
        st.markdown("""
        <div class='header-container'>
            <h1>LARISSA CAMPOS CARDOSO</h1>
            <h2 class='subtitle'>AI Developer & FullStack Engineer</h2>
            <p class='intro-text'>
                Developer specialized in <strong>Artificial Intelligence</strong> and <strong>Machine Learning</strong> 
                with expertise in Python, intelligent chatbot creation, and web development.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Contact Information")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='contact-info'>
            📞 <strong>(34) 98423-7431</strong>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='contact-info'>
            📧 <strong>larissacamposcardoso@gmail.com</strong>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='contact-info'>
            📍 <strong>Uberlândia - MG, Brazil</strong>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='contact-info'>
            🔗 <a href='https://www.linkedin.com/in/larissa-campos-cardoso-a70284239' target='_blank' style='color: #00f0ff;'>LinkedIn</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='contact-info'>
            💻 <a href='https://github.com/LPMLarica' target='_blank' style='color: #00f0ff;'>GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='contact-info'>
            🎓 <a href='https://web.dio.me/users/larissacamposcardoso/?tab=achievements' target='_blank' style='color: #00f0ff;'>Cursos e Estudos</a>
        </div>
        """, unsafe_allow_html=True)
    
    # CV
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col2:
        cv_download = get_cv_download()
        if cv_download:
            st.markdown(cv_download, unsafe_allow_html=True)
        else:
            st.error("Resume not found. Check the file path.")
    
    with col4:
        cover_download = get_cover_download()
        if cover_download:
            st.markdown(cover_download, unsafe_allow_html=True)
        else:
            st.error("Cover Letter not found. Check the file path.")

    # About
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Professional Profile")
    st.markdown("""
    <div class='skill-card'>
        <p style='font-size: 1.2rem;'>
        Developer with strong command of <strong style='color: #00f0ff;'>Python</strong> and specialized interest 
        in <strong style='color: #8a2be2;'>Artificial Intelligence and Machine Learning</strong>. 
        Proven experience in system development, intelligent solutions creation, and participation in hackathons focused on technological innovation.
        </p>
        <p style='font-size: 1.1rem;'>
        ✨ <strong>Highlights:</strong> 3D Modeling with Blender | Frontend Development | Dual Italian Citizenship
        </p>
        <p style='font-size: 1.1rem;'>
        🌍 <strong>Languages:</strong> Portuguese (Native) | Fluent English | Basic French
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills chart
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Skills Map")
    
    fig, skills = create_skills_radar()
    st.plotly_chart(fig, width='stretch')
    
    # Strongest skill
    max_skill = max(skills, key=skills.get)
    max_value = skills[max_skill]
    
    st.markdown(f"""
    <div class='skill-card' style='background: linear-gradient(135deg, rgba(0, 240, 255, 0.2) 0%, rgba(138, 43, 226, 0.2) 100%);'>
        <h3 style='margin: 0;'>🏆 Highlight Skill</h3>
        <p style='font-size: 1.3rem; margin-top: 1rem;'>
            My top expertise is in <strong style='color: #00f0ff; font-size: 1.5rem;'>{max_skill}</strong> 
            with a proficiency level of <strong style='color: #8a2be2; font-size: 1.5rem;'>{max_value}%</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional Experience
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Professional Experience")
    
    experiences = [
        {
            "year": "2025",
            "title": "FullStack AI Developer",
            "company": "GOB Solutions",
            "description": "Development of an intelligent chatbot using Python, integrating IBM MCP Server with EspoCRM API, data cleaning, and Google Gemini connection."
        },
        {
            "year": "2025",
            "title": "Learning Tutor",
            "company": "UNITRI",
            "description": "Support to students with hardware and software issues, teaching support classes in Object-Oriented Programming."
        },
        {
            "year": "2025",
            "title": "AI Developer",
            "company": "Biofy Hackathon",
            "description": "Development of an intelligent chatbot using Langflow and Python, focused on natural language processing solutions."
        },
        {
            "year": "2024",
            "title": "Frontend Developer",
            "company": "Sonner",
            "description": "Development of web applications using JavaScript and Angular, focusing on intuitive and responsive interfaces."
        },
        {
            "year": "2024",
            "title": "Speaker",
            "company": "GRVA",
            "description": "Speaker at IEEVR and University of Florida, sharing experiences in virtual reality projects and technological development."
        },
        {
            "year": "2024",
            "title": "Web Developer",
            "company": "CGW",
            "description": "Corporate website development using JavaScript, HTML, and CSS."
        },
        {
            "year": "2023",
            "title": "Developer",
            "company": "Forja Dev",
            "description": "Programming with GitHub and development in Golang for collaborative projects."
        }
    ]
    
    for exp in experiences:
        st.markdown(f"""
        <div class='experience-card'>
            <h3 style='margin: 0; color: #00f0ff;'>{exp['title']}</h3>
            <p style='color: #8a2be2; font-weight: bold; margin: 0.5rem 0;'>
                {exp['company']} | {exp['year']}
            </p>
            <p style='margin-top: 1rem;'>{exp['description']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Projects
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Featured Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='skill-card'>
            <h3> Intelligent Chatbots</h3>
            <p>Development of AI automation solutions for business processes and training.</p>
            <p><strong>Tech:</strong> Python, Langflow, IBM MCP, Google Gemini, EspoCRM</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='skill-card'>
            <h3> Web Applications</h3>
            <p>Creation of responsive interfaces and complete corporate systems.</p>
            <p><strong>Tech:</strong> JavaScript, Angular, HTML, CSS</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='skill-card'>
            <h3> Virtual Reality and Games</h3>
            <p>Technical translation and presentations at international VR events.</p>
            <p><strong>Tech:</strong> Unity, Blender, 3D Modeling</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='skill-card'>
            <h3> Events & Lectures</h3>
            <p>Participation in LatinoWare, NASA Space Apps, IEEVR, CISTI, and various tech events.</p>
            <p><strong>Locations:</strong> Brazil, Orlando-FL, various academic events</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Academic Background")
    
    st.markdown("""
    <div class='skill-card'>
        <h3 style='color: #00f0ff;'>Bachelor’s in Computer Science</h3>
        <p><strong>Centro Universitário do Triângulo</strong> | 2023 - 2027</p>
    </div>
    
    <div class='skill-card'>
        <h3 style='color: #00f0ff;'>FCE - English Fluency Course</h3>
        <p><strong>Cultura Inglesa, Uberlândia</strong> | 2011 - 2021</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Technical Stack
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
    st.markdown("## Tech Stack")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='skill-card'>
            <h4 style='color: #00f0ff;'>Programing Languages</h4>
            <ul>
                <li>Python ⭐⭐⭐⭐⭐</li>
                <li>JavaScript ⭐⭐⭐⭐</li>
                <li>Golang ⭐⭐⭐</li>
                <li>HTML/CSS ⭐⭐⭐</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='skill-card'>
            <h4 style='color: #8a2be2;'>AI & Frameworks</h4>
            <ul>
                <li>Machine Learning</li>
                <li>Langflow</li>
                <li>Angular</li>
                <li>Streamlit</li>
                <li>EspoCRM</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='skill-card'>
            <h4 style='color: #00f0ff;'>Tools</h4>
            <ul>
                <li>GitHub/Git</li>
                <li>Blender 3D</li>
                <li>Unity</li>
                <li>VS Code</li>
                <li>PyCharm</li>
                <li>Jira/Confluence</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "Certificates":
    st.markdown("<h1 style='text-align: center;'>CERTIFICATES AND ACHIEVEMENTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='skill-card' style='text-align: center;'>
        <h3 style='color: #00f0ff;'>My Professional Certificates and Achievements</h3>
    </div>
    """, unsafe_allow_html=True)

    def display_certificate_grid(certificates, cols=2):
        for i in range(0, len(certificates), cols):
            columns = st.columns(cols)
            for j, col in enumerate(columns):
                if i + j < len(certificates):
                    cert = certificates[i + j]
                    with col:
                        st.markdown("<div class='certificate-card'>", unsafe_allow_html=True)
                        try:
                            if cert.endswith('.pdf'):
                                st.markdown(f"<p style='text-align: center;'>📄 {cert.split('/')[-1]}</p>", unsafe_allow_html=True)
                            else:
                                st.image(cert, use_container_width=True)
                        except Exception as e:
                            st.error(f"Error loading certificate: {cert}. Error: " + str(e))
                        st.markdown("</div>", unsafe_allow_html=True)

    certificates = [
        str(Path("certificados") / "357d50a1-29e2-4105-92f1-4fb8104c928e.png"),
        str(Path("certificados") / "e5c2ab92-44a5-4fed-bc8a-a549f63b2987.png"),
        str(Path("certificados") / "64abd841-a690-4240-a7ae-0ff5f9edcc48.png"), 
        str(Path("certificados") / "24fd469e-068a-486a-b126-40e1b8e2de88.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 124956.png"),
        str(Path("certificados") / "Captura de tela 2025-10-31 154910.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125004.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125016.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125047.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125057.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125113.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125124.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125135.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125150.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125158.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125211.png"),
        str(Path("certificados") / "Captura de tela 2025-10-30 125211.png"),
        str(Path("certificados") / "a00a37e5-ad50-4c55-b7b7-a7c199f3f3cb.png"),
        str(Path("certificados") / "b8c57e80-b488-4e7b-a614-43b4e55d229a.png"),
        str(Path("certificados") / "Captura de tela 2025-11-06 105705.png"),
        str(Path("certificados") / "6LEKVRSP.png"),
        str(Path("certificados") / "DXF2JBKG.png"),
        str(Path("certificados") / "EYDSK4U9.png"),
        str(Path("certificados") / "H0PAEGMQ.png"),
        str(Path("certificados") / "LOZ9ARXB.png"),
        str(Path("certificados") / "LWYKFB3E.png"),
        str(Path("certificados") / "LY4RNWDI.png"),
        str(Path("certificados") / "NOF1G2B2.png"),
        str(Path("certificados") / "NRLDWHRI.png"),
        str(Path("certificados") / "OZZULYIB.png"),
        str(Path("certificados") / "PDSZSLSS.png"),
        str(Path("certificados") / "PSEIBBN3.png"),
        str(Path("certificados") / "QIK1CXYO.png"),
        str(Path("certificados") / "RQZHDJRR.png"),
        str(Path("certificados") / "SBLUCZTK.png"),
        str(Path("certificados") / "TPTI1OJX.png"),
        str(Path("certificados") / "W1JQMWEI.png")
    ]
    
    display_certificate_grid(certificates)

st.markdown("<div class='tech-divider'></div>", unsafe_allow_html=True)
st.markdown("""
<div class='footer'>
    <p>© 2025 Larissa Campos | AI Developer & FullStack Engineer</p>
</div>
""", unsafe_allow_html=True)
