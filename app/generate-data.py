import json
import random
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
json_dir = os.path.join(root_dir, "json")
os.makedirs(json_dir, exist_ok=True)

# All topics — now with a single work experiences label
topics = [
    "introduction",
    "skills",
    "skills_nextjs",
    "skills_laravel",
    "skills_python",
    "projects",
    "skills_fullstack",
    "frontend_development",
    "backend_development",
    "tools_workflow",
    "database_auth",
    "ui_consistency",
    "ci_cd",
    "services",
    "commissions",
    "contact",
    "goals",
    "collaboration",
    "learning",
    "work_experiences",
    "current_work"
]

greetings = ["greetings"]
farewells = ["farewell"]

fallback_label = "fallback"

def generate_response(label):
    if label == "greetings":
        return [
            "Hi there! I’m Jemuel H. Cadayona — JEM CDYN for short. I’m a passionate software developer from Southern Leyte, Philippines. Feel free to ask me about my skills, projects, or how we can work together!",
            "Hello! I’m Jemuel H. Cadayona, but you can call me JEM CDYN. I’m here to help you learn about my work, skills, or how I can help bring your ideas to life.",
            "Hey! I’m Jemuel H. Cadayona — a software developer ready to answer any questions you have about my projects, experience, and how we can collaborate."
        ]

    if label == "farewell":
        return [
            "Thank you so much for your time and interest in my work. Let’s definitely keep in touch and explore opportunities to build something amazing together!",
            "I appreciate you reaching out! I’m looking forward to collaborating with you soon. Goodbye for now!",
            "Thanks for chatting with me! I hope we can connect again and create something valuable together."
        ]

    if label == "introduction":
        return [
            "I’m Jemuel H. Cadayona, a dedicated and detail-oriented software developer focused on building modern, scalable web applications that help communities and businesses grow.",
            "I’m Jemuel H. Cadayona — JEM CDYN — a passionate developer from Southern Leyte. I specialize in creating practical, scalable digital solutions for local government and private clients.",
            "I’m Jemuel H. Cadayona, a full-stack developer who designs and builds modern systems that help communities, businesses, and organizations succeed in the digital age."
        ]

    if label == "skills_nextjs":
        return [
            "Next.js is my go-to framework for building fast, SEO-friendly, and scalable web applications. I use server-side rendering, static generation, and robust API routes for optimal performance.",
            "I rely on Next.js for building production-ready, high-performance web apps with server-side rendering, API routes, and great developer experience.",
            "Next.js is my framework of choice for creating modern, scalable sites that rank well and deliver great user experiences."
        ]

    if label == "skills_laravel":
        return [
            "Laravel is my main backend framework. I use it to build secure, maintainable APIs and efficient data-driven applications. I also use Livewire and LighthousePHP for dynamic interfaces and GraphQL.",
            "I love using Laravel to build robust backend systems and APIs, often pairing it with Livewire for dynamic UIs and LighthousePHP for GraphQL endpoints.",
            "Laravel is at the core of my backend stack for creating secure, scalable systems and clean APIs, complemented by Livewire and LighthousePHP for advanced features."
        ]

    if label == "skills_python":
        return [
            "I use Python for automation, data processing, and writing custom backend scripts that make development more efficient.",
            "Python helps me automate tasks and process data smoothly, complementing my main tech stack.",
            "I integrate Python for scripting, automation, and quick backend tasks that streamline my workflow."
        ]

    if label == "skills_fullstack":
        return [
            "As a full-stack developer, I handle both frontend and backend — from designing beautiful interfaces to building secure APIs — delivering production-ready applications end-to-end.",
            "I cover the full development cycle: from clean, responsive UIs to secure and efficient backend systems.",
            "Being full-stack means I manage the whole process — frontend, backend, database, and deployment — ensuring a smooth delivery every time."
        ]

    if label == "frontend_development":
        return [
            "I build responsive, modern frontends using TailwindCSS, Shadcn UI, React.js, Vue.js, Inertia.js, JavaScript, TypeScript, and Next.js. Clean design and great UX are always top priorities.",
            "My frontend work focuses on creating clean, accessible, and maintainable UIs using modern tools like TailwindCSS, Vue.js, and React.",
            "I design beautiful, responsive interfaces with modern stacks like Next.js, TailwindCSS, Shadcn UI, and TypeScript."
        ]

    if label == "backend_development":
        return [
            "On the backend, I build scalable, secure APIs and systems with Laravel, HonoJS, Livewire, PHP 8, and LighthousePHP. I am using Python for AI and Machine Learning.",
            "I develop backend logic and APIs using Laravel, PHP 8, Livewire, HonoJS, and LighthousePHP for robust performance. I am utilizing Python for AI and Machine Learning.",
            "My backend stack includes Laravel, Livewire, LighthousePHP, HonoJS, and PHP 8 to deliver reliable server-side solutions. Also, I am using Python for AI and Machine Learning."
        ]

    if label == "tools_workflow":
        return [
            "My workflow includes Git, GitHub Actions for CI/CD, Vite, Drizzle ORM, and GraphQL — making development faster and cleaner.",
            "I use tools like Git, GitHub Actions, Vite, and GraphQL to keep my workflow organized, efficient, and production-ready.",
            "With Git, CI/CD pipelines, Vite, and Drizzle ORM, I maintain clean code and automate builds and deployments."
        ]

    if label == "database_auth":
        return [
            "I design databases with MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Eloquent ORM. I secure authentication with NextAuth.js, Laravel Breeze, and Sanctum.",
            "My database management covers relational and non-relational systems like MySQL, PostgreSQL, and MongoDB, paired with secure auth using NextAuth.js and Laravel tools.",
            "I work with modern databases and ensure secure, smooth authentication systems for every application."
        ]

    if label == "ui_consistency":
        return [
            "I use Shadcn UI and similar systems to keep my user interfaces consistent, accessible, and maintainable across all projects.",
            "With design systems like Shadcn UI, I ensure that every application has a cohesive, accessible UI that scales easily.",
            "Consistent, reusable UI components are key — I rely on Shadcn UI to deliver accessible, maintainable interfaces."
        ]

    if label == "ci_cd":
        return [
            "I use GitHub Actions to set up CI/CD pipelines, automating testing and deployments for faster, safer production releases.",
            "My CI/CD pipelines with GitHub Actions ensure that code is tested and deployed reliably and quickly.",
            "I implement automated CI/CD workflows using GitHub Actions, speeding up development and ensuring code quality."
        ]

    if label == "services":
        return [
            "I offer modern web dev services: static sites, custom full-stack apps, secure APIs, and integrations — all tailored to your needs.",
            "From static landing pages to full-stack apps and secure API development, I provide a range of services to match any project.",
            "My services include full-stack development, custom APIs, modern static sites, and robust integrations."
        ]

    if label == "commissions":
        return [
            "My commission rates start at ₱5K–₱10K for static sites, ₱15K–₱20K for full-stack basics, ₱25K–₱50K for standard systems, and ₱60K–₱100K for premium solutions. Refer to the commission section for more details.",
            "I offer flexible pricing: ₱5K–₱10K for static websites, ₱15K–₱20K for basic full-stack, ₱25K–₱50K for student/business systems, ₱60K–₱100K for larger projects. Refer to the commission section for more details.",
            "Project rates range from ₱5K for simple sites to ₱100K for enterprise-level systems — all tailored to your goals and requirements. Refer to the commission section for more details."
        ]

    if label == "contact":
        return [
            "Want to collaborate or ask questions? Visit my contact page — I’m always happy to discuss new ideas and projects.",
            "Ready to start something new? Reach out through my contact section — let’s build your vision together.",
            "You can reach me through my contact area — I’m excited to connect and hear your ideas!"
        ]

    if label == "goals":
        return [
            "My goal is to build practical, high-quality solutions that help clients grow, work smarter, and succeed online.",
            "I aim to deliver real, meaningful results for my clients — solutions that drive growth and efficiency.",
            "My main goal is to provide quality software that solves problems and supports long-term success."
        ]

    if label == "collaboration":
        return [
            "Collaboration matters to me — I love working with students, startups, and government offices to bring ideas to life.",
            "I’m always open to collaborative work. Together, we can turn your vision into a real, working solution.",
            "Partnerships and teamwork are vital — I’m ready to listen and help make your goals a reality."
        ]
    if label == "projects":
        return [
            "I have developed a range of practical, production-ready systems and starter kits to serve various sectors, communities, and local governments. For modern web development, my NextJS Starter Kit provides a comprehensive foundation for building Next.js applications with built-in authentication powered by NextAuth.js, a PostgreSQL database, and a robust stack featuring HonoJS, TailwindCSS, Shadcn UI, TypeScript, GraphQL, TanStack Query, and Supabase for streamlined workflows and scalable deployments. "
            "For local governance, I built the Legislative Management System, a complete solution for municipalities to manage legislative documents and transactions efficiently, using VueJS, InertiaJS, Laravel, TailwindCSS, TypeScript, GraphQL, and TanStack Query. The Document Tracking Assistant, deployed for the Province of Southern Leyte, allows staff to track documents and transactions via QR codes, powered by Laravel, Livewire, MySQL, and JavaScript. "
            "I also designed e-Mercado, a fully featured online store with product management and a shopping cart for the Province of Southern Leyte, built with Laravel, Bootstrap 5, JavaScript, and MySQL. For educational institutions, I created the GJTVS Enrolment & Attendance Management System (RFID)—an integrated enrolment and RFID-based attendance tracker built with Laravel, Livewire, Bootstrap 5, JavaScript, and MySQL. "
            "Supporting public safety, I developed the BFP Information Management System, a complete MIS for the Bureau of Fire Protection with inspection scheduling and SMS appointment features, using VueJS, InertiaJS, Laravel, MySQL, and Pushbullet API. The STMG Road Traffic Offense Management System tracks driver records and penalties using VueJS, InertiaJS, Laravel, and MySQL, while the Municipal Crime & Accident Management System records crimes and accidents with GIS mapping powered by Leaflet, and real-time incident tracking via SMS, built on Laravel, Livewire, Bootstrap 5, JavaScript, MySQL, Leaflet, and Pushbullet API. "
            "In education, the ALS Learners Progress Monitoring System helps the Department of Education track the development of ALS learners, built using Laravel, Livewire, Bootstrap 5, JavaScript, and MySQL. Lastly, I designed and deployed a clean, simple commercial website for Southern Comfort Pensionne, using HTML5, CSS3, Bootstrap 5, and JavaScript to provide essential online presence for the business."
        ]
    if label == "learning":
        return [
            "I’m passionate about continuous learning—exploring new tools, frameworks, and best practices to keep my skills sharp and my projects up-to-date with the latest industry standards."
        ]
    if label == "work_experiences":
        return [
            "I’ve led and contributed to several impactful projects. As a Software Developer and Consultant at Provincial Systems A.O., I built enterprise-level web apps using Laravel, Vue.js, and TailwindCSS. "
            "I optimized complex database structures, improving application load times by 40% and reducing deployment time by 60% through CI/CD pipelines.\n\n"
            "In January 2025, I conducted a full implementation and user demonstration of the Document Tracking Assistant at the Capitol Site Southern Leyte, ensuring staff adoption and smooth operation.\n\n"
            "Previously, in November 2024, I led training sessions to introduce the Document Tracking System to improve transparency and efficiency.\n\n"
            "In April 2024, I held an orientation for the Legislative Management System at Southern Leyte State University, supporting streamlined legislative workflows.\n\n"
            "A key project is the e-Mercado platform launched in June 2023, a digital marketplace supporting local vendors in Southern Leyte. After presenting it to provincial leaders, we enhanced the system based on community feedback in November 2024. "
            "These experiences underscore my commitment to building practical, community-focused technology solutions."
        ]
    if label == "skills":
        return [
            (
                "I have a broad skill set spanning frontend and backend development. On the frontend, I work extensively with Next.js, React.js, Vue.js, Inertia.js, TypeScript, JavaScript, TailwindCSS, and Shadcn UI to craft responsive, maintainable user interfaces. "
                "On the backend, I develop scalable and secure APIs and server logic using Laravel, PHP 8, Livewire.js, LighthousePHP, and HonoJS. I also use Python for AI and Machine Learning. "
                "For databases, I manage MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel's Eloquent ORM, ensuring efficient data handling and security. "
                "I implement robust authentication systems with NextAuth.js, Laravel Breeze, and Sanctum. "
                "To streamline workflows and deployments, I use Git, GitHub Actions, Vite, and GraphQL, all contributing to delivering clean, maintainable, and scalable full-stack applications."
            )
        ]
    if label == "current_work":
        return [
            (
                "Currently, I serve as a Software Developer and Consultant at the Provincial "
                "Systems Administrators Office, Provincial Government of Southern Leyte. In this "
                "role, I have led the development of enterprise-level web applications, including the "
                "Document Tracking Assistant, a robust system designed to streamline the "
                "tracking of official documents and transactions through QR code technology, "
                "tailored specifically for the Province of Southern Leyte. "
                "I was also involved in the development of e-Mercado, a full-featured online "
                "marketplace equipped with product management and a secure shopping cart "
                "system to support local commerce. This project was developed in collaboration with "
                "Southern Leyte State University (SLSU), particularly with Mr. Nestnie Honrada, "
                "highlighting a strong partnership between the provincial government and the "
                "academic sector."
            )
    ]
    return [
        "I’m not sure how to answer that yet — feel free to ask me anything about my work, skills, or commission offers!"
    ]


# Training examples
data = []
responses = []

# Greetings & farewells
for _ in range(50):
    data.append({"text": random.choice(["Hi!", "Hello!", "Hey!", "Greetings!"]), "label": "greetings"})
    data.append({"text": random.choice(["Goodbye!", "See you!", "Bye!", "Catch you later!", "Thank you", "Thanks"]), "label": "farewell"})

questions = {
    "current_work": [
    "what is your work",
    "what is your current job",
    "tell me about your current work",
    "what's your role right now",
    "what's your current role",
    "where do you work",
    "who do you work for",
    "what company do you work for",
    "what is your current position",
    "are you working now",
    "what are you doing now",
    ],
    "introduction": [
        "Can you tell me about yourself?",
        "Who are you?",
        "Please introduce yourself.",
        "What should I know about you?",
        "Tell me about yourself.",
        "Introduce yourself to me.",
        "Who is JEM CDYN?",
        "What is your name?",
        "Your name please?",
        "May I know your name?",
        "Tell me your name.",
        "What do you call yourself?",
        "What’s your bio?"
    ],
    "projects": [
        "What are your projects?",
        "What projects have you done?",
        "Can you tell me about your projects?",
        "What kind of projects have you built?",
        "What have you worked on?",
        "Show me your projects.",
        "Do you have any project examples?",
        "What are some of your past projects?",
        "Can you share your project portfolio?",
        "List some projects you made.",
        "Tell me about your project work.",
        "Tell me about the systems you built.",
        "Any projects you can show?",
        "Projects?",
        "What project?",
        "What proejc",
        "What did you develop?",
        "Do you have project samples?",
        "Give me examples of your projects.",
        "What solutions have you delivered?",
        "What projects have you built?",
        "Tell me about your past projects.",
        "Can you share some project examples?",
        "What have you worked on?",
        "What was your latest project?",
        "What’s your biggest project?",
        "Can you describe your projects?",
        "What type of projects do you prefer?"
    ],
    "skills_nextjs": [
        "Do you work with Next.js?",
        "What can you do with Next.js?",
        "Tell me about your Next.js skills.",
        "Are you good at Next.js?",
        "How do you use Next.js?",
        "What is your experience with Next.js?",
        "Do you build apps with Next.js?",
        "Do you use Next.js for production?"
    ],
    "skills_laravel": [
        "Are you experienced with Laravel?",
        "What Laravel projects have you done?",
        "Tell me about your Laravel skills.",
        "Do you use Laravel for backend?",
        "How long have you used Laravel?",
        "Do you build APIs with Laravel?",
        "Are you good at Laravel?",
        "What do you like about Laravel?"
    ],
    "skills_python": [
        "Do you know Python?",
        "What do you build with Python?",
        "Tell me about your Python experience.",
        "Do you use Python for development?",
        "What’s your Python skill level?",
        "Are you comfortable coding Python?",
        "Do you build scripts in Python?",
        "How often do you use Python?"
    ],
    "skills_fullstack": [
        "Are you a full-stack developer?",
        "Can you handle full-stack projects?",
        "Do you work on frontend and backend?",
        "Tell me about your full-stack development.",
        "Do you do full-stack work?",
        "What is your full-stack experience?",
        "How good are you at full-stack projects?",
        "What stacks do you use for full-stack work?"
    ],
    "frontend_development": [
        "What frontend technologies do you use?",
        "How do you build modern frontends?",
        "Are you good at frontend development?",
        "What do you use for designing UIs?",
        "How do you make responsive interfaces?",
        "Tell me about your frontend tools.",
        "How do you handle frontend design?",
        "What frameworks do you use for frontend?"
    ],
    "backend_development": [
        "What backend frameworks do you use?",
        "Tell me about your backend experience.",
        "How do you build APIs?",
        "Are you good with backend development?",
        "How do you structure backend code?",
        "What do you prefer for backend work?",
        "Do you use Laravel or HonoJS for backend?",
        "How do you secure your backend?"
    ],
    "tools_workflow": [
        "What tools do you use for development?",
        "Do you use Git or GitHub Actions?",
        "Tell me about your workflow.",
        "How do you manage deployments?",
        "Do you use Vite or GraphQL?",
        "How do you handle version control?",
        "What’s your typical workflow?",
        "Do you automate your workflow?"
    ],
    "database_auth": [
        "What databases do you use?",
        "How do you handle authentication?",
        "Tell me about your database design.",
        "Do you build login systems?",
        "How do you secure user accounts?",
        "What ORM do you use for databases?",
        "Do you work with MySQL or MongoDB?",
        "How do you manage user auth?"
    ],
    "ui_consistency": [
        "How do you maintain UI consistency?",
        "Do you use design systems?",
        "Tell me about Shadcn UI.",
        "How do you keep your interfaces consistent?",
        "What do you use for design standards?",
        "Do you use component libraries?",
        "How do you handle UI patterns?",
        "Do you build custom UI kits?"
    ],
    "ci_cd": [
        "Do you use CI/CD pipelines?",
        "How do you deploy your projects?",
        "Tell me about your deployment workflow.",
        "Do you automate deployments?",
        "What’s your CI/CD process?",
        "Do you use GitHub Actions for CI/CD?",
        "How do you push to production?",
        "Do you have automated tests?"
    ],
    "services": [
        "What services do you offer?",
        "How can you help clients?",
        "Tell me about your development services.",
        "Do you offer web development?",
        "What can I hire you for?",
        "Do you build custom websites?",
        "Do you offer consulting?",
        "What do you provide to businesses?"
    ],
    "commissions": [
        "Do you accept commissions?",
        "What are your rates?",
        "Tell me about your pricing.",
        "Where can I see your commission details?",
        "How much do you charge?",
        "What’s your pricing structure?",
        "What’s your starting price?",
        "Where do I find your rates?"
    ],
    "contact": [
        "How can I contact you?",
        "Can I reach you for a project?",
        "Where do I get in touch?",
        "How do I send you a message?",
        "How do I reach you?",
        "What’s the best way to contact you?",
        "Where can I send an inquiry?",
        "Do you have a contact form?"
    ],
    "goals": [
        "What is your goal as a developer?",
        "Tell me about your main goals.",
        "What do you aim to achieve?",
        "What are you working towards?",
        "What’s your professional goal?",
        "What motivates you?",
        "Where do you see yourself going?",
        "What’s your mission as a developer?"
    ],
    "collaboration": [
        "Are you open to collaboration?",
        "Can we work together?",
        "Do you collaborate with others?",
        "How do you handle partnerships?",
        "Can I work with you?",
        "Are you open for joint projects?",
        "Do you do teamwork?",
        "Do you like partnering with others?"
    ],
    "learning": [
        "Do you like learning new tech?",
        "How do you keep improving?",
        "Tell me about your learning process.",
        "Do you stay updated with trends?",
        "How do you learn new tools?",
        "What do you do to stay current?",
        "Do you take courses?",
        "How do you upgrade your skills?"
    ],
    "work_experiences": [
        "Tell me about your work experience.",
        "What are your experience",
        "What are your experiences",
        "Your experience",
        "Your experiences",
        "What jobs have you done?",
        "Can you share your work history?",
        "What have you worked on as a developer?",
        "Where have you worked?",
        "What companies have you worked for?",
        "Can you describe your career?",
        "What’s your professional background?"
    ],
    "skills": [
        "What are your skills?",
        "Can you tell me about your skills?",
        "What technologies do you know?",
        "What programming languages and tools do you use?",
        "List your skills.",
        "What frameworks do you work with?",
        "What tech stack do you use?",
        "What’s your technical skill set?"
    ]
}

for topic, qs in questions.items():
    for _ in range(30):  # 30 samples per topic for good balance
        q = random.choice(qs)
        data.append({"text": q, "label": topic})

# Fallback noise
for i in range(100):
    nonsense = f"random noise {i} zxcvb"
    data.append({"text": nonsense, "label": fallback_label})

# Add all other labels to responses
for label in topics + greetings + farewells:
    responses.append({"label": label, "response": generate_response(label)})

# Add fallback responses
fallback_responses = [
    f"Sorry, I don't know how to respond to that yet — maybe ask about my projects, skills, or commissions!"
    for i in range(1, 21)
]
responses.append({"label": fallback_label, "response": fallback_responses})

data_path = os.path.join(json_dir, "data.json")
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Save responses.json inside json folder
responses_path = os.path.join(json_dir, "responses.json")
with open(responses_path, "w", encoding="utf-8") as f:
    json.dump(responses, f, indent=2)

print(f"✅ Done! Created {len(data)} data items and {len(responses)} response labels.")
