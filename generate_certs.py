import json

certs = [
    {"name": "🛡️ Fortinet Certified Fundamentals (FCF)", "issuer": "Fortinet", "date": "Jul 2026"},
    {"name": "☁️ Oracle Certified Foundations Assoc.", "issuer": "Oracle", "date": "Jul 2026"},
    {"name": "🔐 Application Security Analyst", "issuer": "Reliance Foundation", "date": "Apr 2026"},
    {"name": "🌐 Cybersecurity Fundamentals", "issuer": "IBM", "date": "Apr 2026"},
    {"name": "🕵️ Online Fraud Prevention Specialist", "issuer": "Hack &amp; Fix", "date": "May 2026"},
    {"name": "🛡️ CompTIA Security+", "issuer": "KodeKloud", "date": "Feb 2026 – 2030"},
    {"name": "💻 CCPP — C++ Practitioner", "issuer": "Red Team Leaders", "date": "Feb 2026"},
    {"name": "🎓 CCEP — Cybersecurity Educator", "issuer": "Red Team Leaders", "date": "Feb 2026"},
    {"name": "💼 Deloitte Cyber Job Simulation", "issuer": "Forage", "date": "Apr 2026"},
    {"name": "💼 Tata Cybersecurity Analyst Job Sim.", "issuer": "Forage", "date": "Apr 2026"},
    {"name": "🕵️‍♂️ Ethical Hacker — Course Completion", "issuer": "Cisco Networking", "date": "2026"},
    {"name": "🔒 Cyber Security Course Completion", "issuer": "Smarted (STEM)", "date": "2026"},
    {"name": "🌐 ITS — HTML &amp; CSS", "issuer": "Pearson VUE", "date": "Dec 2025 – 2029"},
]

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 680" width="850" height="680">
  <defs>
    <style>
      
      .bg { fill: #0d1117; rx: 15px; stroke: #7C3AED; stroke-width: 2px; }
      .bg-glow { fill: none; stroke: #A855F7; stroke-width: 6px; filter: blur(8px); rx: 15px; }
      
      .title { font-family: 'Fira Code', monospace; font-size: 26px; font-weight: 600; fill: #A855F7; text-anchor: middle; filter: drop-shadow(0 0 8px #7C3AED); }
      .header { font-family: 'Fira Code', monospace; font-size: 16px; font-weight: 600; fill: #00E5FF; }
      .header-glow { font-family: 'Fira Code', monospace; font-size: 16px; font-weight: 600; fill: #00E5FF; filter: drop-shadow(0 0 5px #00E5FF); }
      
      .text-name { font-family: 'Fira Code', monospace; font-size: 14.5px; fill: #E2E8F0; font-weight: 600; }
      .text-issuer { font-family: 'Fira Code', monospace; font-size: 14px; fill: #94A3B8; }
      .text-date { font-family: 'Fira Code', monospace; font-size: 14px; fill: #FBBF24; text-anchor: end; font-weight: 600; }
      
      .line { stroke: #1F2937; stroke-width: 1px; }
      .hover-box:hover { fill: #1F2937; opacity: 0.5; }
      
      /* Animations */
      .row { opacity: 0; animation: slideIn 0.6s ease forwards; transform: translateX(-30px); }
      
      @keyframes slideIn {
        to { opacity: 1; transform: translateX(0); }
      }
      @keyframes pulse {
        0%, 100% { filter: drop-shadow(0 0 5px #7C3AED); }
        50% { filter: drop-shadow(0 0 15px #A855F7); }
      }
      .title-pulse { animation: pulse 3s infinite; }
    </style>
  </defs>

  <!-- Background with glow -->
  <rect class="bg-glow" x="10" y="10" width="830" height="660" />
  <rect class="bg" x="10" y="10" width="830" height="660" />
  
  <text x="425" y="55" class="title title-pulse">🏆 CERTIFICATIONS &amp; ACHIEVEMENTS 🏆</text>

  <line x1="30" y1="80" x2="820" y2="80" class="line" />
  
  <text x="40" y="110" class="header-glow">CERTIFICATION</text>
  <text x="480" y="110" class="header-glow">ISSUER</text>
  <text x="810" y="110" class="header-glow" style="text-anchor: end;">DATE</text>

  <line x1="30" y1="130" x2="820" y2="130" class="line" />
"""

y_start = 170
spacing = 38

for i, cert in enumerate(certs):
    y = y_start + (i * spacing)
    delay = 0.3 + (i * 0.15)
    
    svg_content += f"""
  <g class="row" style="animation-delay: {delay}s;">
    <!-- Hover Background -->
    <rect x="30" y="{y-24}" width="790" height="{spacing}" fill="transparent" class="hover-box" rx="5"/>
    
    <!-- Text Elements -->
    <text x="40" y="{y}" class="text-name">{cert['name']}</text>
    <text x="480" y="{y}" class="text-issuer">{cert['issuer']}</text>
    <text x="810" y="{y}" class="text-date">{cert['date']}</text>
    
    <!-- Divider line -->
    <line x1="30" y1="{y+10}" x2="820" y2="{y+10}" class="line" stroke-dasharray="4" opacity="0.3"/>
  </g>
"""

svg_content += "</svg>"

with open("assets/certifications.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
    
print("Successfully generated assets/certifications.svg")
