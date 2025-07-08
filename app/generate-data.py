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
            (
                "I have developed a range of practical, production-ready systems and starter kits that serve various sectors, communities, and local governments. "
                "For modern web development, my NextJS Starter Kit provides a solid foundation for building Next.js applications with built-in authentication powered by NextAuth.js, a PostgreSQL database, and a robust stack including HonoJS, TailwindCSS, Shadcn UI, TypeScript, GraphQL, TanStack Query, and Supabase for streamlined workflows and scalable deployments. "
                "For local governance, I created the Legislative Management System — a full-featured solution for municipalities to handle legislative documents and transactions efficiently, built with VueJS, InertiaJS, Laravel, TailwindCSS, TypeScript, GraphQL, and TanStack Query. The Document Tracking Assistant, developed for the Province of Southern Leyte, lets staff track documents and transactions via QR codes, using Laravel, Livewire, MySQL, and JavaScript. "
                "I also built e-Mercado, an online store with product management and a shopping cart for the Province of Southern Leyte, powered by Laravel, Bootstrap 5, JavaScript, and MySQL. For schools, I developed the GJTVS Enrolment & Attendance Management System (RFID) — a comprehensive enrolment and attendance tracker using RFID, Laravel, Livewire, Bootstrap 5, JavaScript, and MySQL. "
                "To support public safety, I built the BFP Information Management System for the Bureau of Fire Protection, featuring inspection scheduling and SMS-enabled appointments with VueJS, InertiaJS, Laravel, MySQL, and Pushbullet API. I also created the STMG Road Traffic Offense Management System to track driver records and penalties using VueJS, InertiaJS, Laravel, and MySQL, and the Municipal Crime & Accident Management System, which records incidents and shows GIS mapping via Leaflet, using Laravel, Livewire, Bootstrap 5, JavaScript, MySQL, Leaflet, and Pushbullet API. "
                "For education, the ALS Learners Progress Monitoring System helps the Department of Education track the development of ALS learners, built using Laravel, Livewire, Bootstrap 5, JavaScript, and MySQL. Lastly, I designed and deployed a clean commercial website for Southern Comfort Pensionne using HTML5, CSS3, Bootstrap 5, and JavaScript to build a simple yet effective online presence."
            ),
            (
                "My portfolio covers impactful systems and starter kits for multiple sectors. The NextJS Starter Kit offers a modern base for Next.js projects with NextAuth.js, PostgreSQL, HonoJS, TailwindCSS, Shadcn UI, TypeScript, GraphQL, TanStack Query, and Supabase for fast deployment. "
                "For local governments, I developed the Legislative Management System, a complete solution for managing legislative documents and transactions, built with VueJS, InertiaJS, Laravel, TailwindCSS, TypeScript, GraphQL, and TanStack Query. The Document Tracking Assistant for Southern Leyte enables QR-based document tracking using Laravel, Livewire, MySQL, and JavaScript. "
                "I launched e-Mercado for local online selling, developed the GJTVS Enrolment & Attendance Management System for RFID-based student tracking, the BFP Information Management System for inspections and SMS scheduling, and the STMG Road Traffic Offense Management System to manage driver records and penalties. "
                "Additionally, the Municipal Crime & Accident Management System records incidents and maps locations with Leaflet, while the ALS Learners Progress Monitoring System supports the Department of Education. For small businesses, I delivered a simple yet effective website for Southern Comfort Pensionne using clean HTML, CSS, and Bootstrap."
            ),
            (
                "I have designed a series of robust, real-world systems and starter kits for a variety of use cases. For modern full-stack projects, my NextJS Starter Kit includes everything needed for scalable Next.js development: NextAuth.js, PostgreSQL, HonoJS, TailwindCSS, Shadcn UI, TypeScript, GraphQL, TanStack Query, and Supabase. "
                "In the public sector, I built the Legislative Management System for municipal document handling and the Document Tracking Assistant for the Province of Southern Leyte to simplify tracking using QR codes — all powered by VueJS, InertiaJS, Laravel, Livewire, MySQL, and JavaScript. "
                "Other projects include e-Mercado for local commerce, the GJTVS Enrolment & Attendance Management System with RFID, the BFP Information Management System with SMS scheduling, the STMG Road Traffic Offense Management System for traffic monitoring, and the Municipal Crime & Accident Management System that uses Leaflet maps for incident reports. "
                "I also created the ALS Learners Progress Monitoring System for DepEd and delivered a simple commercial website for Southern Comfort Pensionne using HTML5, CSS3, Bootstrap 5, and JavaScript for an effective online presence."
            )
        ]

    if label == "learning":
        return [
            "I’m passionate about continuous learning—exploring new tools, frameworks, and best practices to keep my skills sharp and my projects up-to-date with the latest industry standards.",
            "Learning never stops for me. I constantly seek out new technologies, techniques, and best practices to ensure my skills stay relevant and my work delivers real value.",
            "I believe in lifelong learning — I regularly experiment with new frameworks, libraries, and workflows so my projects benefit from fresh ideas and modern solutions.",
            "I make it a priority to stay updated with the latest tech trends, tools, and development practices, which helps me bring innovative, reliable solutions to every project I work on."
        ]
    if label == "work_experiences":
        return [
            (
                "I’ve led and contributed to impactful projects as a Software Developer and Consultant at the Provincial Systems Administrators Office. "
                "I developed large-scale web applications using Laravel, Vue.js, and TailwindCSS, and optimized complex databases — boosting load speeds by 40% and cutting deployment times by 60% with CI/CD pipelines.\n\n"
                "In January 2025, I deployed and demonstrated the Document Tracking Assistant for the Capitol Site in Southern Leyte, helping staff adopt it smoothly.\n\n"
                "Earlier, in November 2024, I led training for the Document Tracking System to increase transparency and efficiency.\n\n"
                "In April 2024, I organized an orientation for the Legislative Management System at Southern Leyte State University to help local offices streamline legislative work.\n\n"
                "One highlight is the e-Mercado project — a digital marketplace for Southern Leyte launched in June 2023 and enhanced later that year based on community feedback. "
                "These experiences show my commitment to delivering meaningful, practical tech solutions for local communities."
            ),
            (
                "Throughout my career as a Software Developer and Consultant at Provincial Systems A.O., I’ve built enterprise-level web solutions with Laravel, Vue.js, and TailwindCSS. "
                "I improved database structures to enhance performance by 40 percent and streamlined deployments with CI/CD, cutting rollout time by 60%.\n\n"
                "In January 2025, I fully implemented the Document Tracking Assistant at the Capitol Site, training staff for smooth onboarding. "
                "In November 2024, I led training sessions for the Document Tracking System to boost document processing transparency. "
                "In April 2024, I conducted an orientation for the Legislative Management System at Southern Leyte State University.\n\n"
                "I also launched the e-Mercado project in June 2023 — a digital platform to support local vendors — and improved it later that year to better meet community needs. "
                "These milestones highlight my dedication to solving real problems through technology."
            ),
            (
                "As a Software Developer and Consultant for Provincial Systems A.O., I’ve handled significant projects that impacted local government operations. "
                "I engineered robust web apps with Laravel, Vue.js, and TailwindCSS, and optimized database systems to speed up load times by 40% while implementing CI/CD pipelines that reduced deployment times by 60%.\n\n"
                "In January 2025, I rolled out the Document Tracking Assistant for the Southern Leyte Capitol Site and guided staff through its use. "
                "Before that, in November 2024, I organized user training for the Document Tracking System to ensure better document tracking and transparency. "
                "In April 2024, I held an orientation session for the Legislative Management System at SLSU to help offices handle legislative tasks efficiently.\n\n"
                "One standout project is e-Mercado, launched in June 2023 to support local commerce and improved later that year with community-driven updates. "
                "These experiences highlight my drive to deliver tech that directly benefits communities."
            )
        ]
    if label == "skills":
        return [
            (
                "I have a broad skill set that covers both frontend and backend development. "
                "On the frontend, I specialize in building responsive and maintainable user interfaces using Next.js, React.js, Vue.js, Inertia.js, TypeScript, JavaScript, TailwindCSS, and Shadcn UI. "
                "For backend development, I build secure and scalable APIs and server-side logic with Laravel, PHP 8, Livewire.js, LighthousePHP, and HonoJS — plus Python for AI and automation. "
                "I manage data using MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel’s Eloquent ORM to keep systems efficient and secure. "
                "My authentication implementations rely on NextAuth.js for Next.js projects and Breeze or Sanctum for Laravel. "
                "To ensure smooth development workflows, I use Git, GitHub Actions, Vite, and GraphQL, delivering clean, production-ready full-stack solutions."
            ),
            (
                "My technical skill set spans the entire stack. On the frontend side, I build sleek, responsive interfaces with Next.js, React.js, Vue.js, Inertia.js, TypeScript, JavaScript, TailwindCSS, and Shadcn UI. "
                "The backend side includes developing robust APIs and server logic with Laravel, PHP 8, Livewire.js, LighthousePHP, and HonoJS, plus using Python for AI tasks and automation. "
                "I work with databases like MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel’s Eloquent ORM to keep data secure and well-structured. "
                "Authentication is handled with NextAuth.js for Next.js and Breeze or Sanctum for Laravel. "
                "I also integrate Git, GitHub Actions, Vite, and GraphQL to maintain clean workflows and automate builds and deployments."
            ),
            (
                "I’m skilled in a wide range of technologies covering full-stack web development. "
                "My frontend expertise includes Next.js, React.js, Vue.js, Inertia.js, TypeScript, JavaScript, TailwindCSS, and Shadcn UI for building modern and responsive interfaces. "
                "For backend development, I rely on Laravel, PHP 8, Livewire.js, LighthousePHP, HonoJS, and Python for specialized tasks like AI and automation. "
                "I manage data efficiently with MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel's Eloquent ORM. "
                "For authentication, I use NextAuth.js with Next.js and Breeze or Sanctum for Laravel applications. "
                "I also automate my workflow with Git, GitHub Actions, Vite, and use GraphQL for streamlined APIs, ensuring my solutions stay clean, maintainable, and scalable."
            ),
            (
                "My skill set combines modern frontend frameworks and robust backend technologies. "
                "On the frontend, I use Next.js, React.js, Vue.js, Inertia.js, TypeScript, JavaScript, TailwindCSS, and Shadcn UI to design responsive, reusable interfaces. "
                "On the backend, I develop secure, efficient APIs and services with Laravel, PHP 8, Livewire.js, LighthousePHP, HonoJS, and Python for automation and AI-related tasks. "
                "For databases, I handle MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel's Eloquent ORM to manage data safely and effectively. "
                "Authentication solutions rely on NextAuth.js for Next.js and Laravel Breeze or Sanctum for Laravel. "
                "To streamline my development pipeline, I use Git, GitHub Actions, Vite, and GraphQL — making my full-stack projects scalable, maintainable, and production-ready."
            )
        ]
    if label == "current_work":
        return [
            (
                "Currently, I am working as a Software Developer and Consultant at the Provincial "
                "Systems Administrators Office under the Provincial Government of Southern Leyte. "
                "In this role, I lead the development of large-scale web applications like the "
                "Document Tracking Assistant, which streamlines tracking official documents and transactions "
                "using QR code technology for the province. I also contributed to building e-Mercado, "
                "an online marketplace with product management and a secure shopping cart, created in "
                "partnership with Southern Leyte State University (SLSU) and Mr. Nestnie Honrada."
            ),
            (
                "I am currently serving as a Software Developer and Consultant for the Provincial "
                "Systems Administrators Office of the Provincial Government of Southern Leyte. "
                "My work includes developing robust systems such as the Document Tracking Assistant, "
                "which simplifies how government documents are tracked and processed with QR codes. "
                "I also helped build e-Mercado, a full-fledged online marketplace that supports local "
                "businesses — a project done together with Southern Leyte State University (SLSU) and "
                "Mr. Nestnie Honrada."
            ),
            (
                "At present, I work as a Software Developer and Consultant at the Provincial "
                "Systems Administrators Office for the Provincial Government of Southern Leyte. "
                "I have led the development of the Document Tracking Assistant — a system designed "
                "to make tracking official documents more efficient using QR code scanning. "
                "In addition, I helped create e-Mercado, a secure online store for local commerce, "
                "in close collaboration with Southern Leyte State University (SLSU) and Mr. Nestnie Honrada."
            ),
            (
                "Right now, I am a Software Developer and Consultant for the Provincial "
                "Systems Administrators Office, Provincial Government of Southern Leyte. "
                "I spearheaded the Document Tracking Assistant project, which improves how the province "
                "handles document tracking through QR codes. Another key project I contributed to is "
                "e-Mercado — an online marketplace supporting local sellers, built together with "
                "Southern Leyte State University (SLSU) and Mr. Nestnie Honrada."
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
    data.append({"text": random.choice(["Hi", "Hello", "Hey", "Greetings", "Hii", "Helloo", "Heyy", "Good morning", "Good day", "Good afternoon", "Good evening"]), "label": "greetings"})
    data.append({"text": random.choice(["Goodbye!", "See you!", "Bye!", "Catch you later!", "Thank you", "Thanks"]), "label": "farewell"})

questions = {
    "current_work": [
        "what is your work",
        "what is your current job",
        "tell me about your current work",
        "what is your role right now",
        "what is your current role",
        "where do you work",
        "who do you work for",
        "what company do you work for",
        "what is your current position",
        "are you working now",
        "are you working",
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
        "What is your bio?"
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
        "What is your biggest project?",
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
        "What is your Python skill level?",
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
        "What is your typical workflow?",
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
        "What is your pricing structure?",
        "What is your starting price?",
        "Where do I find your rates?"
    ],
    "contact": [
        "How can I contact you?",
        "Can I reach you for a project?",
        "Where do I get in touch?",
        "How do I send you a message?",
        "How do I reach you?",
        "What is the best way to contact you?",
        "Where can I send an inquiry?",
        "Do you have a contact form?"
    ],
    "goals": [
        "What is your goal as a developer?",
        "Tell me about your main goals.",
        "What do you aim to achieve?",
        "What are you working towards?",
        "What is your professional goal?",
        "What motivates you?",
        "Where do you see yourself going?",
        "What is your mission as a developer?"
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
        "What is your professional background?"
    ],
    "skills": [
        "What are your skills?",
        "Can you tell me about your skills?",
        "What technologies do you know?",
        "What programming languages and tools do you use?",
        "List your skills.",
        "What frameworks do you work with?",
        "What tech stack do you use?",
        "What is your technical skill set?"
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

for response_obj in responses:
    label = response_obj.get("label")
    if label and label in questions:
        # Insert questions into this response object
        response_obj["questions"] = questions[label]
        
# Add fallback responses
fallback_responses = [
    f"Sorry, I don't know how to respond to that yet — maybe ask about my projects, skills, or commissions!"
    for i in range(1, 21)
]
responses.append({"label": fallback_label, "response": fallback_responses})

data_path = os.path.join(json_dir, "data.json")
responses_path = os.path.join(json_dir, "responses.json")

# Delete existing files if they exist
if os.path.exists(data_path):
    os.remove(data_path)

if os.path.exists(responses_path):
    os.remove(responses_path)

# Write new files
with open(data_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open(responses_path, "w", encoding="utf-8") as f:
    json.dump(responses, f, indent=2)

print(f"✅ Done! Created {len(data)} data items and {len(responses)} response labels.")
