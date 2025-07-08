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
    "skills_fullstack",
    "frontend_development",
    "backend_development",
    "tools_workflow",
    "database_auth",
    "ui_consistency",
    "ci_cd",
    "projects",
    "services",
    "commissions",
    "contact",
    "goals",
    "collaboration",
    "learning",
    "work_experiences"  # 👈 single topic for all work history
]

greetings = ["greetings"]
farewells = ["farewell"]

fallback_label = "fallback"

def generate_response(label):
    if label == "greetings":
        return [
            "Hi there! I’m Jemuel H. Cadayona — JEM CDYN for short. "
            "I’m a passionate software developer from Southern Leyte, Philippines. "
            "Feel free to ask me about my skills, past work, projects, or how we can collaborate to bring your ideas to life!"
        ]
    if label == "farewell":
        return [
            "Thank you so much for your time and interest in my work. "
            "Let’s definitely keep in touch and explore opportunities to build something amazing together!"
        ]
    if label == "introduction":
        return [
            "I’m Jemuel H. Cadayona, a dedicated and detail-oriented software developer focused on creating modern, scalable web applications. "
            "My work supports local communities, government offices, and businesses in thriving digitally by improving their systems and workflows."
        ]
    if label == "skills_nextjs":
        return [
            "Next.js is my preferred framework for building fast, SEO-friendly, and scalable web applications. "
            "I leverage its server-side rendering, static site generation, and powerful API routes to deliver robust user experiences."
        ]
    if label == "skills_laravel":
        return [
            "Laravel is my core backend framework where I build secure, maintainable APIs and data-driven systems. "
            "I integrate it with Livewire for dynamic UI components and LighthousePHP for building flexible GraphQL APIs."
        ]
    if label == "skills_python":
        return [
            "I use Python for automation, data processing, and custom backend scripts that enhance development efficiency and system capabilities."
        ]
    if label == "skills_fullstack":
        return [
            "As a full-stack developer, I cover the entire spectrum—from crafting beautiful, responsive frontends to building reliable, secure backends—ensuring seamless end-to-end application delivery."
        ]
    if label == "frontend_development":
        return [
            "My frontend expertise includes creating responsive and accessible user interfaces using TailwindCSS, Shadcn UI, React.js, Vue.js, Inertia.js, JavaScript, TypeScript, and Next.js. "
            "I focus on clean design, excellent user experience, and maintainability."
        ]
    if label == "backend_development":
        return [
            "On the backend, I develop scalable APIs and systems with Laravel, HonoJS, Livewire, PHP 8, and LighthousePHP, ensuring performance, security, and reliability."
        ]
    if label == "tools_workflow":
        return [
            "I rely on modern tools like Git, GitHub Actions for CI/CD, Vite for fast builds, Drizzle ORM for efficient database handling, and GraphQL for clean API design—streamlining the entire development process."
        ]
    if label == "database_auth":
        return [
            "I design and manage databases with MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel's Eloquent ORM. "
            "For authentication, I implement secure, user-friendly login systems using NextAuth.js in Next.js and Breeze or Sanctum in Laravel."
        ]
    if label == "ui_consistency":
        return [
            "Using design systems like Shadcn UI, I maintain consistent, accessible, and maintainable user interfaces across complex applications, improving usability and developer experience."
        ]
    if label == "ci_cd":
        return [
            "I build CI/CD pipelines with GitHub Actions to automate testing, building, and deployment, enabling fast, reliable delivery of production-ready applications."
        ]
    if label == "projects":
        return [
            "I have worked on diverse projects—from internal management systems for government offices to community e-commerce platforms—always focusing on solving real problems with practical, user-centric solutions."
        ]
    if label == "services":
        return [
            "I offer comprehensive web development services including modern static websites, custom full-stack applications, secure API development, and third-party integrations tailored to client needs."
        ]
    if label == "commissions":
        return [
            "My commission rates start at ₱5,000 to ₱10,000 for static websites, ₱15,000 to ₱20,000 for basic full-stack development, ₱25,000 to ₱50,000 for standard student or business systems, "
            "and ₱60,000 to ₱100,000 for premium or enterprise-level projects. Please check my commission section for detailed information."
        ]
    if label == "contact":
        return [
            "Ready to start a project or just want to say hi? Visit my contact section to get in touch—I’m always excited to discuss new ideas and collaborations."
        ]
    if label == "goals":
        return [
            "My main goal is to deliver high-quality, practical software solutions that empower clients to grow, optimize workflows, and thrive in the digital landscape."
        ]
    if label == "collaboration":
        return [
            "I value collaboration deeply. Whether you’re a startup, student, or government agency, I’m eager to listen, understand your needs, and work together to make your vision a reality."
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
                "On the backend, I develop scalable and secure APIs and server logic using Laravel, PHP 8, Livewire.js, LighthousePHP, and HonoJS. "
                "For databases, I manage MySQL, PostgreSQL, MongoDB, Drizzle ORM, Supabase, and Laravel's Eloquent ORM, ensuring efficient data handling and security. "
                "I implement robust authentication systems with NextAuth.js, Laravel Breeze, and Sanctum. "
                "To streamline workflows and deployments, I use Git, GitHub Actions, Vite, and GraphQL, all contributing to delivering clean, maintainable, and scalable full-stack applications."
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
    "projects": [
        "What projects have you built?",
        "Tell me about your past projects.",
        "Can you share some project examples?",
        "What have you worked on?",
        "What was your latest project?",
        "What’s your biggest project?",
        "Can you describe your projects?",
        "What type of projects do you prefer?"
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
