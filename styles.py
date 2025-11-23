"""
Centralized UI Styling Module
Modern design system with dark themes, glassmorphism, and vibrant accents
"""

import streamlit as st

def inject_custom_css():
    """Inject comprehensive custom CSS for modern UI design"""
    st.markdown("""
    <style>
    /* Import Modern Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* CSS Variables - Design System */
    :root {
        --primary: hsl(250, 100%, 65%);
        --primary-light: hsl(250, 100%, 75%);
        --primary-dark: hsl(250, 100%, 55%);
        --secondary: hsl(200, 100%, 55%);
        --secondary-light: hsl(200, 100%, 65%);
        --accent: hsl(320, 100%, 60%);
        --accent-light: hsl(320, 100%, 70%);
        --success: hsl(140, 70%, 55%);
        --warning: hsl(40, 100%, 60%);
        --danger: hsl(0, 80%, 60%);
        --bg-dark: hsl(240, 20%, 8%);
        --bg-darker: hsl(240, 25%, 5%);
        --glass: rgba(255, 255, 255, 0.08);
        --glass-border: rgba(255, 255, 255, 0.15);
        --text-primary: hsl(0, 0%, 95%);
        --text-secondary: hsl(0, 0%, 70%);
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
        --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
        --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
        --glow-primary: 0 0 20px rgba(139, 92, 246, 0.5);
        --glow-accent: 0 0 20px rgba(236, 72, 153, 0.5);
    }
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, 
            hsl(240, 20%, 8%) 0%, 
            hsl(250, 30%, 12%) 25%,
            hsl(240, 20%, 8%) 50%,
            hsl(260, 25%, 10%) 75%,
            hsl(240, 20%, 8%) 100%
        );
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
    }
    
    @keyframes gradientShift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Animated Background Particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 70%, rgba(59, 130, 246, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 50% 50%, rgba(236, 72, 153, 0.08) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    
    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.025em;
    }
    
    p, span, div {
        font-family: 'Inter', sans-serif;
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    code {
        font-family: 'JetBrains Mono', monospace;
        background: rgba(139, 92, 246, 0.1);
        padding: 0.2em 0.4em;
        border-radius: 4px;
        font-size: 0.9em;
    }
    
    /* Main Container */
    .main > div {
        padding: 2rem 1rem;
        position: relative;
        z-index: 1;
    }
    
    /* Glassmorphic Cards */
    .glass-card {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 16px;
        padding: 2rem;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            var(--glass-border), 
            transparent
        );
    }
    
    .glass-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg), var(--glow-primary);
        border-color: var(--primary);
    }
    
    /* Hero Section */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, 
            var(--primary) 0%, 
            var(--secondary) 50%, 
            var(--accent) 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1rem;
        animation: shimmer 3s ease-in-out infinite;
        background-size: 200% 200%;
    }
    
    @keyframes shimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        text-align: center;
        color: var(--text-secondary);
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Feature Cards */
    .feature-card {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        padding: 2rem;
        text-align: center;
        backdrop-filter: blur(20px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, 
            transparent, 
            rgba(139, 92, 246, 0.1), 
            transparent
        );
        transform: rotate(45deg);
        transition: all 0.5s;
    }
    
    .feature-card:hover::before {
        top: -100%;
        left: -100%;
    }
    
    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: var(--primary);
        box-shadow: 0 12px 40px rgba(139, 92, 246, 0.3);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 10px currentColor);
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    .feature-card h4 {
        font-size: 1.25rem;
        margin-bottom: 0.75rem;
        color: var(--text-primary);
    }
    
    .feature-card p {
        font-size: 0.95rem;
        color: var(--text-secondary);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        font-family: 'Poppins', sans-serif;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-md);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.2);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton > button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg), var(--glow-primary);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--primary), var(--accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-size: 0.85rem;
    }
    
    [data-testid="stMetricDelta"] {
        font-weight: 600;
    }
    
    div[data-testid="metric-container"] {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        padding: 1.5rem;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-md), var(--glow-primary);
        border-color: var(--primary);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: var(--glass);
        border: 2px dashed var(--glass-border);
        border-radius: 16px;
        padding: 3rem 2rem;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: var(--primary);
        background: rgba(139, 92, 246, 0.05);
        box-shadow: var(--glow-primary);
    }
    
    [data-testid="stFileUploader"] section {
        border: none;
        background: transparent;
    }
    
    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"] button:hover {
        transform: scale(1.05);
        box-shadow: var(--glow-primary);
    }
    
    /* Progress Bars */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--primary), var(--accent));
        border-radius: 10px;
        box-shadow: var(--glow-primary);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .stProgress > div > div {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    
    /* Info/Success/Warning/Error Boxes */
    .stAlert {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        backdrop-filter: blur(20px);
        padding: 1rem 1.5rem;
    }
    
    [data-baseweb="notification"] {
        background: var(--glass);
        border-left-width: 4px;
        border-radius: 8px;
        backdrop-filter: blur(20px);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, 
            hsl(240, 25%, 10%) 0%, 
            hsl(240, 20%, 8%) 100%
        );
        border-right: 1px solid var(--glass-border);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: var(--text-secondary);
    }
    
    /* Dividers */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent, 
            var(--glass-border), 
            transparent
        );
        margin: 2rem 0;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 8px;
        backdrop-filter: blur(20px);
        font-weight: 600;
        color: var(--text-primary);
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: var(--primary);
        box-shadow: var(--glow-primary);
    }
    
    .streamlit-expanderContent {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-top: none;
        border-radius: 0 0 8px 8px;
        backdrop-filter: blur(20px);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--glass);
        border-radius: 12px;
        padding: 0.5rem;
        backdrop-filter: blur(20px);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px;
        color: var(--text-secondary);
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(139, 92, 246, 0.1);
        color: var(--primary);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        box-shadow: var(--glow-primary);
    }
    
    /* Images */
    img {
        border-radius: 12px;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
    }
    
    img:hover {
        transform: scale(1.02);
        box-shadow: var(--shadow-lg), var(--glow-primary);
    }
    
    /* Dataframe/Table */
    [data-testid="stDataFrame"] {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        backdrop-filter: blur(20px);
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: var(--primary);
        border-right-color: var(--secondary);
        border-bottom-color: var(--accent);
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-darker);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        border-radius: 10px;
        border: 2px solid var(--bg-darker);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, var(--primary-light), var(--secondary-light));
    }
    
    /* Custom Classes for HTML Markdown */
    .neon-text {
        color: var(--primary);
        text-shadow: 0 0 10px var(--primary), 0 0 20px var(--primary);
    }
    
    .gradient-text {
        background: linear-gradient(135deg, var(--primary), var(--accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-card {
        background: var(--glass);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        padding: 1.5rem;
        backdrop-filter: blur(20px);
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-md), var(--glow-primary);
        border-color: var(--primary);
    }
    
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        box-shadow: var(--shadow-sm);
    }
    
    /* Loading Animation */
    @keyframes shimmerLoading {
        0% { background-position: -1000px 0; }
        100% { background-position: 1000px 0; }
    }
    
    .loading-shimmer {
        animation: shimmerLoading 2s infinite linear;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(139, 92, 246, 0.2), 
            transparent
        );
        background-size: 1000px 100%;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .hero-subtitle {
            font-size: 1rem;
        }
        
        .feature-card {
            padding: 1.5rem;
        }
        
        .glass-card {
            padding: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def create_hero_section(title, subtitle):
    """Create an animated hero section with gradient title"""
    st.markdown(f"""
    <div style="text-align: center; padding: 3rem 0 2rem 0;">
        <h1 class="hero-title">{title}</h1>
        <p class="hero-subtitle">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def create_feature_card(icon, title, description):
    """Create a glassmorphic feature card"""
    return f"""
    <div class="feature-card">
        <div class="feature-icon">{icon}</div>
        <h4>{title}</h4>
        <p>{description}</p>
    </div>
    """


def create_stat_card(label, value, icon=""):
    """Create a statistics card"""
    return f"""
    <div class="stat-card">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="font-size: 2rem; font-weight: 700; 
                    background: linear-gradient(135deg, var(--primary), var(--accent));
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;">
            {value}
        </div>
        <div style="color: var(--text-secondary); font-size: 0.9rem; 
                    font-weight: 600; text-transform: uppercase; 
                    letter-spacing: 0.05em; margin-top: 0.5rem;">
            {label}
        </div>
    </div>
    """


def create_badge(text, color="primary"):
    """Create a styled badge"""
    return f'<span class="badge">{text}</span>'


def create_gradient_divider():
    """Create a gradient divider line"""
    st.markdown('<hr>', unsafe_allow_html=True)
