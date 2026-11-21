
import html
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Asma | Creative Portfolio",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

ROOT = Path(__file__).parent
MEDIA = ROOT / "assets"

# Professional details adapted from Asma's CV.
# Confirm which contact details she wants publicly visible before deployment.
PROFILE = {
    "name": "Asma'a Alhabaibeh",
    "headline": "Ideas made visual.",
    "subtitle": "Graphic Design · AI-Assisted Creativity · Branding · Motion · UI/UX",
    "about": (
        "I'm a graphic designer based in Amman, Jordan, with 4+ years of "
        "experience creating brand-focused visuals, social media campaigns, "
        "presentations, and motion content. I use AI tools to explore concepts "
        "and accelerate production, then refine each piece with Adobe creative "
        "tools to ensure the final result is polished, purposeful, and on-brand. "
        "My background in UX and bilingual Arabic–English design helps me "
        "create work that is clear, accessible, and audience-focused."
    ),
    "location": "Amman, Jordan",
    "email": "asma2000sameer@gmail.com",
    "phone": "+962 79 726 7030",
    "languages": "Arabic (native) · English (proficient)",
    "education": "Bachelor's Degree in Graphic Design · Al Ahliyya Amman University (2021)",
    "behance": "",
    "instagram": "",
}

EXPERIENCE = [
    {
        "role": "Graphic Designer",
        "company": "Optimiza",
        "period": "Nov 2022 – Present",
        "summary": "Social campaigns, marketing and web banners, AI-assisted creative production, presentations, and website interface refinements in Figma.",
    },
    {
        "role": "Graphic Designer",
        "company": "Tarjama",
        "period": "Aug 2022 – Nov 2022",
        "summary": "Presentations and proposals, editorial redesign, and bilingual social content. Client presentation work is confidential and not shown here.",
    },
    {
        "role": "Creative Graphic Designer",
        "company": "Jo Academy",
        "period": "Dec 2021 – Jul 2022",
        "summary": "Social media artwork and production graphics for an online education platform, working alongside the production team.",
    },
]

SPECIALTIES = [
    "Branding & visual identity",
    "Social media design & motion graphics",
    "AI-assisted design & creative prompting",
    "Presentations & proposals",
    "Bilingual Arabic–English & RTL layouts",
    "UI/UX & digital design",
]

TOOLS = [
    "Adobe Photoshop · Illustrator · InDesign",
    "After Effects · Premiere Pro",
    "Figma · Adobe XD · WordPress",
    "HTML · CSS · Google Analytics",
    "AI image & video generation tools",
]

# Projects grouped by client and theme
PROJECTS = [
    {
        "title": "Markazia Toyota",
        "categories": ["Campaigns", "UI/UX"],
        "type": "Automotive · Social · Motion · UI/UX",
        "description": (
            "Automotive campaign visuals, service-focused motion "
            "content, and vehicle service history UX design."
        ),
        "images": [
            "toyota_roads.jpg",
            "toyota_technology.jpg",
        ],
        "videos": ["toyota_service.mp4"],
        "ux": True,
        "figma_url": "https://www.figma.com/design/HgtwSUDQnySl1BIcXk5207/Markazia-%E2%80%93-Vehicle-Service-History--UX-task-?node-id=28-342&p=f&t=X7L1eRRlJJSg8592-0",
    },
    {
        "title": "Reflect",
        "categories": ["Campaigns"],
        "type": "Financial services · Social & motion",
        "description": (
            "A coordinated collection of banking card designs "
            "and a student-fees motion campaign."
        ),
        "images": [
            "reflect_credit.jpg",
            "reflect_debit.jpg",
            "reflect_virtual.jpg",
        ],
        "videos": ["reflect_fees.mp4"],
    },
    {
        "title": "ABC · Karak · Solidarity",
        "categories": ["Social Design"],
        "type": "Social media · Campaigns",
        "description": (
            "Social media artwork featuring local identity, "
            "cultural storytelling, and campaign messaging."
        ),
        "images": [
            "abc_story.jpg",
            "karak_post.jpg",
            "solidarity_national.jpg",
            "solidarity_injaz.jpg",
        ],
        "videos": [],
    },
    {
        "title": "Aman Insurance",
        "categories": ["Social Design"],
        "type": "Insurance · Digital campaign",
        "description": "Insurance-focused digital campaign artwork.",
        "images": ["aman_insurance.jpg"],
        "videos": [],
    },
    {
        "title": "BLK",
        "categories": ["Motion"],
        "type": "Short-form brand video",
        "description": "Short-form branded video content.",
        "images": [],
        "videos": ["blk.mp4"],
    },
    {
        "title": "Digital Transformation",
        "categories": ["Motion"],
        "type": "Web banner · Motion",
        "description": "Wide-format digital banner animation.",
        "images": [],
        "videos": ["web_banner.mp4"],
    },
]

# Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --paper: #faf9f7;
    --ink: #1d1b1b;
    --muted: #77716e;
    --accent: #df5a40;
    --line: #e8e4e0;
}

[data-testid="stAppViewContainer"] {
    background: var(--paper);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1160px;
    padding-top: 2.3rem;
    padding-bottom: 5rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif;
    letter-spacing: -.048em;
    color: var(--ink);
}

p {
    color: var(--muted);
}

.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--line);
    padding-bottom: 22px;
    margin-bottom: 65px;
}

.logotype {
    font-family: 'Manrope', sans-serif;
    font-size: 25px;
    letter-spacing: -.07em;
    font-weight: 800;
    color: var(--ink);
}

.righttag {
    font-size: 11px;
    letter-spacing: .18em;
    font-weight: 700;
    color: #817b77;
}

.eyebrow {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 18px;
}

.hero {
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    letter-spacing: -.075em;
    line-height: 1.03;
    font-size: clamp(50px, 7vw, 97px);
    color: var(--ink);
    max-width: 940px;
    margin: 0 0 24px;
}

.hero em {
    font-style: normal;
    color: var(--accent);
}

.subtitle {
    font-size: 18px;
    line-height: 1.75;
    color: #6c6662;
    max-width: 650px;
    margin-bottom: 65px;
}

.rule {
    border-top: 1px solid var(--line);
    margin: 38px 0;
}

.section-title {
    font-family: 'Manrope', sans-serif;
    font-size: 39px;
    font-weight: 800;
    letter-spacing: -.06em;
    margin-bottom: 20px;
    color: var(--ink);
}

.project-name {
    font-family: 'Manrope', sans-serif;
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -.045em;
    color: var(--ink);
    margin-top: 10px;
}

.project-meta {
    color: #8b847f;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .1em;
    font-size: 11px;
    margin: 5px 0 12px;
}

.project-desc {
    font-size: 14px;
    line-height: 1.65;
    color: #716b67;
    margin-bottom: 16px;
}

/* Apply the same gallery dimensions to BOTH images and videos. 
   object-fit: contain preserves the full artwork without cropping. */
div[class*="st-key-gallery_"] [data-testid="stImage"],
div[class*="st-key-gallery_"] [data-testid="stVideo"] {
    height: 420px !important;
    min-height: 420px !important;
    max-height: 420px !important;
    background: #eeebe7;
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

div[class*="st-key-gallery_"] [data-testid="stImage"] img {
    width: 100% !important;
    height: 420px !important;
    object-fit: contain !important;
    border-radius: 10px;
}

div[class*="st-key-gallery_"] [data-testid="stVideo"] > div {
    width: 100% !important;
    height: 100% !important;
    aspect-ratio: auto !important;
}

div[class*="st-key-gallery_"] [data-testid="stVideo"] video {
    width: 100% !important;
    height: 420px !important;
    object-fit: contain !important;
    background: #eeebe7;
    border-radius: 10px;
}

[data-testid="stTabs"] button {
    font-family: 'DM Sans', sans-serif;
    font-weight: 700;
}

/* Gallery navigation buttons */
div.stButton > button {
    border: 1px solid var(--line);
    background: #ffffff;
    color: var(--ink);
    border-radius: 10px;
    font-size: 20px;
    min-height: 43px;
    transition: background .2s, border-color .2s;
}

div.stButton > button:hover {
    background: #fceeea;
    border-color: var(--accent);
    color: var(--accent);
}

/* Figma button - red background, white text */
[data-testid="stLinkButton"] a {
    background-color: #c43648 !important;
    border: none !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* White text inside the button */
[data-testid="stLinkButton"] a * {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* Darker red on hover */
[data-testid="stLinkButton"] a:hover {
    background-color: #a92c3d !important;
    color: #ffffff !important;
}

div.stLinkButton a:hover,
div.stLinkButton a:hover p,
div.stLinkButton a:hover span {
    color: #ffffff !important;
}

.slide-counter {
    text-align: center;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: #77716e;
}

/* Professional information */
.about-intro {
    max-width: 850px;
    font-size: 16px;
    line-height: 1.9;
    color: #625b57;
    margin-bottom: 30px;
}
.info-title {
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
    color: var(--ink);
    font-size: 21px;
    letter-spacing: -.035em;
    margin-bottom: 12px;
}
.experience-entry {
    padding: 15px 0;
    border-bottom: 1px solid var(--line);
}
.experience-role {
    color: var(--ink);
    font-size: 15px;
    font-weight: 700;
}
.experience-period { color: #8b847f; font-size: 12px; margin-top: 3px; }
.experience-detail { color: #716b67; font-size: 13px; line-height: 1.7; margin-top: 7px; }
.portfolio-tag {
    display: inline-block;
    margin: 0 6px 9px 0;
    padding: 7px 12px;
    border: 1px solid var(--line);
    border-radius: 30px;
    font-size: 12px;
    color: #5f5955;
    background: #ffffff;
}
.contact-link, .contact-link:visited { color: #ffffff !important; -webkit-text-fill-color: #ffffff !important; }
.contact-link:hover { text-decoration: underline; }

.contact {
    background: #242323;
    padding: 36px 42px;
    border-radius: 16px;
    margin-top: 25px;
    color: #fff;
}

.contact-title {
    font-family: 'Manrope', sans-serif;
    color: #fff;
    font-size: 37px;
    font-weight: 800;
    letter-spacing: -.06em;
}

.contact p, .contact a {
    color: #e0d9d5;
}

.footer {
    font-size: 12px;
    color: #8a817c;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid var(--line);
}

@media(max-width:650px) {
    .block-container {
        padding-top: 1rem;
    }

    .topbar {
        margin-bottom: 35px;
    }

    .subtitle {
        font-size: 16px;
        margin-bottom: 35px;
    }

    .section-title {
        font-size: 31px;
    }

    .contact {
        padding: 25px;
    }
    div[class*="st-key-gallery_"] [data-testid="stImage"],
    div[class*="st-key-gallery_"] [data-testid="stVideo"],
    div[class*="st-key-gallery_"] [data-testid="stImage"] img,
    div[class*="st-key-gallery_"] [data-testid="stVideo"] video {
        height: 280px !important;
        min-height: 280px !important;
        max-height: 280px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    f"""
    <div class="topbar">
        <span class="logotype">
            {html.escape(PROFILE["name"])}
            <span style="color:#df5a40">.</span>
        </span>
        <span class="righttag">CREATIVE PORTFOLIO / 2026</span>
    </div>
    """,
    unsafe_allow_html=True
)

# Hero
st.markdown(
    '<div class="eyebrow">Selected creative work</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero">Ideas made <em>visual.</em></div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">{html.escape(PROFILE["subtitle"])}</div>',
    unsafe_allow_html=True
)

# Projects
st.markdown(
    """
    <div class="rule"></div>
    <div class="section-title">
        Selected projects<span style="color:#df5a40">.</span>
    </div>
    """,
    unsafe_allow_html=True
)

categories = [
    "All work",
    "Campaigns",
    "Social Design",
    "Motion",
    "UI/UX",
]

selected = st.segmented_control(
    "Browse work",
    categories,
    default="All work",
    label_visibility="collapsed"
) or "All work"

shown = [
    p for p in PROJECTS
    if selected == "All work" or selected in p["categories"]
]


def show_project(p):
    """Display a project with its own navigable media gallery."""

    slides = []

    # Add images
    for filename in p["images"]:
        slides.append({
            "kind": "image",
            "path": MEDIA / "images" / filename,
        })

    # Add videos
    for filename in p["videos"]:
        slides.append({
            "kind": "video",
            "path": MEDIA / "videos" / filename,
        })

    # Add the UX case study pages to Markazia
    if p.get("ux", False):
        for i in range(1, 8):
            slides.append({
                "kind": "image",
                "path": MEDIA / "ux" / f"screen_{i}.jpg",
            })

    # Keep only existing files
    slides = [
        slide for slide in slides
        if slide["path"].is_file()
    ]

    # Stable project-specific session state
    key = (
        "slide_"
        + p["title"].lower()
        .replace(" ", "_")
        .replace("·", "_")
    )

    if key not in st.session_state:
        st.session_state[key] = 0

    if not slides:
        st.info("Project media will be added soon.")
    else:
        index = st.session_state[key] % len(slides)
        current = slides[index]

        # Fixed-size gallery container: consistent height when slides change.
        with st.container(key=f"gallery_{key}"):
            if current["kind"] == "image":
                st.image(str(current["path"]), use_container_width=True)
            elif current["kind"] == "video":
                st.video(str(current["path"]))

        # Previous / next navigation
        if len(slides) > 1:

            previous, counter, next_slide = st.columns(
                [1, 2, 1],
                vertical_alignment="center"
            )

            with previous:
                if st.button(
                    "❮",
                    key=f"{key}_prev",
                    use_container_width=True
                ):
                    st.session_state[key] = (
                        index - 1
                    ) % len(slides)
                    st.rerun()

            with counter:
                st.markdown(
                    f'<div class="slide-counter">'
                    f'{index + 1} / {len(slides)}'
                    f'</div>',
                    unsafe_allow_html=True
                )

            with next_slide:
                if st.button(
                    "❯",
                    key=f"{key}_next",
                    use_container_width=True
                ):
                    st.session_state[key] = (
                        index + 1
                    ) % len(slides)
                    st.rerun()

    # Project details
    st.markdown(
        f"""
        <div class="project-name">
            {html.escape(p["title"])}
        </div>
        <div class="project-meta">
            {html.escape(p["type"])}
        </div>
        <div class="project-desc">
            {html.escape(p["description"])}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Direct view-only link instead of a PDF download.
    figma_url = p.get("figma_url", "").strip()
    if figma_url.startswith("https://"):
        st.link_button(
            "View UX Design in Figma ↗",
            figma_url,
            use_container_width=True
        )


# Two-column project layout
for i in range(0, len(shown), 2):

    left, right = st.columns(
        2,
        gap="large",
        vertical_alignment="top"
    )

    with left:
        show_project(shown[i])

    with right:
        if i + 1 < len(shown):
            show_project(shown[i + 1])

    st.write("")


# About
st.markdown(
    '<div class="rule"></div><div class="section-title">A little about me'
    '<span style="color:#df5a40">.</span></div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="about-intro">{html.escape(PROFILE["about"])}</div>',
    unsafe_allow_html=True,
)

# Experience and specialties
experience_col, skills_col = st.columns([1.2, 1], gap="large")
with experience_col:
    st.markdown('<div class="info-title">Experience</div>', unsafe_allow_html=True)
    for job in EXPERIENCE:
        st.markdown(
            '<div class="experience-entry">'
            f'<div class="experience-role">{html.escape(job["role"])} · {html.escape(job["company"])}</div>'
            f'<div class="experience-period">{html.escape(job["period"])}</div>'
            f'<div class="experience-detail">{html.escape(job["summary"])}</div>'
            '</div>',
            unsafe_allow_html=True,
        )

with skills_col:
    st.markdown('<div class="info-title">What I do</div>', unsafe_allow_html=True)
    st.markdown(
        ''.join(f'<span class="portfolio-tag">{html.escape(skill)}</span>' for skill in SPECIALTIES),
        unsafe_allow_html=True,
    )
    st.markdown('<div class="info-title" style="margin-top:24px">Tools</div>', unsafe_allow_html=True)
    for tool in TOOLS:
        st.markdown(f'<div class="experience-detail">{html.escape(tool)}</div>', unsafe_allow_html=True)

st.markdown('<div class="info-title" style="margin-top:25px">Education & languages</div>', unsafe_allow_html=True)
st.markdown(f'**{html.escape(PROFILE["education"])}**')
st.caption(PROFILE["languages"])

# Contact
st.markdown(
    '<div class="contact">'
    '<div class="eyebrow">Let’s collaborate</div>'
    '<div class="contact-title">Have a project in mind?</div>'
    '<p>Open to creative collaborations and new opportunities.</p>'
    f'<p>{html.escape(PROFILE["location"])}</p>'
    f'<p><a class="contact-link" href="mailto:{html.escape(PROFILE["email"], quote=True)}">{html.escape(PROFILE["email"])}</a></p>'
    f'<p><a class="contact-link" href="tel:{html.escape(PROFILE["phone"].replace(" ", ""), quote=True)}">{html.escape(PROFILE["phone"])}</a></p>'
    '</div>',
    unsafe_allow_html=True,
)

if PROFILE["behance"]:
    st.markdown(f'[Behance]({PROFILE["behance"]})')
if PROFILE["instagram"]:
    st.markdown(f'[Instagram]({PROFILE["instagram"]})')

st.markdown(
    f'<div class="footer">© 2026 {html.escape(PROFILE["name"])} · Creative portfolio</div>',
    unsafe_allow_html=True,
)
