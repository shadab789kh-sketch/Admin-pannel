from flask import Flask, render_template_string

app = Flask(__name__)

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>NAWAB KIING | CONTROL PANEL</title>

<link
href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap"
rel="stylesheet">

<style>

/* =========================================================
   RESET
========================================================= */

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

:root{
    --cyan:#00eaff;
    --blue:#1685ff;
    --pink:#ff28d7;
    --green:#25d366;
    --telegram:#0088cc;

    --glass:rgba(3,8,20,.40);
    --glass-dark:rgba(0,0,0,.55);

    --border:rgba(0,234,255,.25);

    --text:#ffffff;
    --muted:#b2bdca;
}

html,
body{
    width:100%;
    min-height:100%;
}

body{

    font-family:'Poppins',sans-serif;

    color:var(--text);

    /*
       BACKGROUND IMAGE
       Replace this URL with your own image if needed.
    */

    background:
        linear-gradient(
            rgba(0,0,0,.20),
            rgba(0,0,0,.30)
        ),
        url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1920&q=90");

    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;

    overflow-x:hidden;
}


/* =========================================================
   BACKGROUND EFFECT
========================================================= */

body::before{

    content:"";

    position:fixed;

    inset:0;

    pointer-events:none;

    background:
        radial-gradient(
            circle at 50% 20%,
            rgba(0,234,255,.12),
            transparent 38%
        );

    z-index:-1;
}


/* =========================================================
   SCROLLBAR
========================================================= */

::-webkit-scrollbar{
    width:7px;
}

::-webkit-scrollbar-track{
    background:rgba(0,0,0,.45);
}

::-webkit-scrollbar-thumb{
    background:rgba(0,234,255,.45);
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:rgba(0,234,255,.8);
}


/* =========================================================
   LOGIN SCREEN
========================================================= */

.login-box{

    width:100%;
    min-height:100vh;

    display:flex;

    flex-direction:column;

    align-items:center;

    justify-content:center;

    padding:25px;

    background:
        rgba(0,0,0,.18);

}


/* LOGIN CARD */

.login-card{

    width:min(430px,92vw);

    padding:35px 28px;

    text-align:center;

    border-radius:24px;

    background:
        rgba(0,0,0,.42);

    border:
        1px solid rgba(0,234,255,.35);

    backdrop-filter:blur(10px);

    box-shadow:

        0 0 25px
        rgba(0,234,255,.12),

        inset 0 0 30px
        rgba(0,234,255,.025);
}


/* LOGO */

.logo{

    width:75px;
    height:75px;

    margin:0 auto 18px;

    display:flex;

    align-items:center;
    justify-content:center;

    border-radius:50%;

    border:
        2px solid var(--cyan);

    color:var(--cyan);

    font-size:23px;

    font-weight:800;

    background:
        rgba(0,0,0,.30);

    box-shadow:

        0 0 15px
        rgba(0,234,255,.55),

        inset 0 0 18px
        rgba(0,234,255,.12);

    text-shadow:
        0 0 10px var(--cyan);
}


/* LOGIN TITLE */

.login-card h1{

    color:var(--cyan);

    font-size:clamp(22px,6vw,32px);

    font-weight:800;

    letter-spacing:1px;

    text-shadow:

        0 0 8px var(--cyan),

        0 0 20px
        rgba(0,234,255,.45);

}


/* SUBTITLE */

.login-card .subtitle{

    margin-top:7px;

    margin-bottom:25px;

    color:var(--muted);

    font-size:9px;

    letter-spacing:2px;

}


/* INPUT GROUP */

.input-group{

    position:relative;

    margin-bottom:14px;

}


/* INPUT */

.input-group input{

    width:100%;

    height:48px;

    padding:
        0 15px;

    border-radius:11px;

    border:
        1px solid
        rgba(0,234,255,.25);

    background:
        rgba(0,0,0,.45);

    color:#fff;

    font-family:inherit;

    font-size:12px;

    outline:none;

    text-align:left;

    transition:.25s;

}


.input-group input::placeholder{

    color:#718096;

}


.input-group input:focus{

    border-color:var(--cyan);

    box-shadow:

        0 0 0 2px
        rgba(0,234,255,.06),

        0 0 15px
        rgba(0,234,255,.18);

}


/* LOGIN BUTTON */

.login-btn{

    width:100%;

    height:48px;

    margin-top:8px;

    border:0;

    border-radius:11px;

    background:
        linear-gradient(
            135deg,
            #00eaff,
            #0875ff
        );

    color:#001018;

    font-family:inherit;

    font-size:12px;

    font-weight:800;

    letter-spacing:1px;

    cursor:pointer;

    transition:.25s;

    box-shadow:
        0 0 18px
        rgba(0,174,255,.25);

}


.login-btn:hover{

    transform:translateY(-2px);

    box-shadow:
        0 0 28px
        rgba(0,174,255,.55);

}


.login-btn:active{

    transform:translateY(0);

}


/* LOGIN ERROR */

.login-error{

    display:none;

    margin-top:13px;

    padding:9px;

    border-radius:8px;

    color:#ff829b;

    background:
        rgba(255,0,70,.08);

    border:
        1px solid
        rgba(255,0,70,.20);

    font-size:9px;

}


/* =========================================================
   MAIN DASHBOARD
========================================================= */

.container{

    display:none;

    width:100%;

    max-width:1100px;

    margin:auto;

    padding:
        18px 15px 35px;

}


/* =========================================================
   TOP NAV
========================================================= */

.navbar{

    display:flex;

    align-items:center;

    justify-content:space-between;

    gap:15px;

    padding:
        12px 16px;

    border-radius:14px;

    background:
        rgba(0,0,0,.38);

    border:
        1px solid
        rgba(255,255,255,.10);

    backdrop-filter:blur(9px);

    box-shadow:
        0 8px 30px rgba(0,0,0,.18);

}


/* BRAND */

.brand{

    display:flex;

    align-items:center;

    gap:10px;

}


.brand-icon{

    width:10px;
    height:10px;

    border-radius:50%;

    background:#00ff9d;

    box-shadow:
        0 0 10px #00ff9d;

}


.brand-name{

    color:#fff;

    font-size:10px;

    font-weight:800;

    letter-spacing:1.5px;

}


/* ONLINE */

.online{

    color:#00ff9d;

    font-size:8px;

    font-weight:700;

    letter-spacing:1px;

}


/* =========================================================
   HERO
========================================================= */

.hero{

    text-align:center;

    padding:
        38px 10px 25px;

}


.hero h1{

    color:var(--cyan);

    font-size:
        clamp(25px,6vw,48px);

    font-weight:800;

    letter-spacing:2px;

    text-shadow:

        0 0 8px var(--cyan),

        0 0 22px
        rgba(0,234,255,.55),

        0 0 45px
        rgba(0,234,255,.22);

}


.hero p{

    margin-top:8px;

    color:#d1d9e5;

    font-size:9px;

    letter-spacing:3px;

}


/* =========================================================
   STATS
========================================================= */

.stats{

    display:grid;

    grid-template-columns:
        repeat(3,1fr);

    gap:10px;

    margin-bottom:15px;

}


.stat{

    padding:13px;

    text-align:center;

    border-radius:12px;

    background:
        rgba(0,0,0,.30);

    border:
        1px solid
        rgba(255,255,255,.09);

    backdrop-filter:blur(7px);

}


.stat-value{

    color:var(--cyan);

    font-size:16px;

    font-weight:800;

}


.stat-label{

    margin-top:2px;

    color:#8996a9;

    font-size:7px;

    letter-spacing:1.5px;

    text-transform:uppercase;

}


/* =========================================================
   SERVICE GRID
========================================================= */

.services{

    display:grid;

    grid-template-columns:
        repeat(2,1fr);

    gap:15px;

}


/* =========================================================
   SERVICE CARD
========================================================= */

.box{

    position:relative;

    padding:25px 20px;

    text-align:center;

    border-radius:18px;

    background:
        rgba(0,0,0,.40);

    border:
        1px solid
        rgba(255,255,255,.10);

    backdrop-filter:blur(8px);

    box-shadow:
        0 10px 35px
        rgba(0,0,0,.20);

    overflow:hidden;

    transition:

        transform .25s,

        border-color .25s,

        box-shadow .25s;

}


/* TOP LINE */

.box::before{

    content:"";

    position:absolute;

    top:0;
    left:0;

    width:80px;
    height:2px;

    background:var(--cyan);

    box-shadow:
        0 0 12px var(--cyan);

}


/* HOVER */

.box:hover{

    transform:
        translateY(-5px);

    border-color:
        rgba(0,234,255,.35);

    box-shadow:

        0 15px 45px
        rgba(0,0,0,.28),

        0 0 25px
        rgba(0,234,255,.08);

}


/* CARD ICON */

.card-icon{

    width:55px;
    height:55px;

    margin:0 auto 13px;

    display:flex;

    align-items:center;
    justify-content:center;

    border-radius:16px;

    background:
        rgba(0,234,255,.07);

    border:
        1px solid
        rgba(0,234,255,.20);

    color:var(--cyan);

    font-size:20px;

}


/* CARD TITLE */

.box h2{

    color:#fff;

    font-size:16px;

    font-weight:700;

    letter-spacing:.3px;

}


/* DESCRIPTION */

.box p{

    min-height:42px;

    margin:
        8px 0 18px;

    color:#aeb8c7;

    font-size:9px;

    line-height:1.6;

}


/* =========================================================
   BUTTON
========================================================= */

.btn{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    min-height:42px;

    width:100%;

    padding:
        10px 15px;

    border:0;

    border-radius:10px;

    text-decoration:none;

    font-size:9px;

    font-weight:800;

    letter-spacing:.7px;

    color:#fff;

    transition:.25s;

}


.btn:hover{

    transform:
        translateY(-2px);

    filter:brightness(1.08);

}


/* COLORS */

.post-btn{

    background:
        linear-gradient(
            135deg,
            #00eaff,
            #0875ff
        );

    color:#001018;

    box-shadow:
        0 0 15px
        rgba(0,234,255,.20);

}


.token-btn{

    background:
        linear-gradient(
            135deg,
            #ff25dc,
            #8e19ff
        );

    box-shadow:
        0 0 15px
        rgba(255,0,220,.18);

}


.combo-btn{

    background:
        linear-gradient(
            135deg,
            #1877f2,
            #0758c9
        );

}


.whatsapp-btn{

    background:
        linear-gradient(
            135deg,
            #25d366,
            #128c4b
        );

}


.telegram-btn{

    background:
        linear-gradient(
            135deg,
            #0088cc,
            #006ca5
        );

}


.instagram-btn{

    background:
        linear-gradient(
            45deg,
            #f09433,
            #e6683c,
            #dc2743,
            #cc2366,
            #bc1888
        );

}


/* =========================================================
   FOOTER
========================================================= */

.footer{

    text-align:center;

    padding:
        25px 5px 5px;

    color:#9ca8b9;

    font-size:8px;

    letter-spacing:1px;

}


.footer span{

    color:var(--cyan);

}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width:700px){

    body{

        background-attachment:
            scroll;

    }


    .container{

        padding:
            10px 10px 25px;

    }


    .navbar{

        padding:
            10px 11px;

    }


    .hero{

        padding:
            27px 5px 19px;

    }


    .hero h1{

        font-size:25px;

    }


    .hero p{

        font-size:7px;

        letter-spacing:2px;

    }


    .services{

        grid-template-columns:1fr;

        gap:10px;

    }


    .box{

        padding:
            20px 16px;

    }


    .box h2{

        font-size:14px;

    }


    .box p{

        min-height:auto;

    }

}


/* SMALL MOBILE */

@media(max-width:400px){

    .stats{

        gap:5px;

    }


    .stat{

        padding:9px 4px;

    }


    .stat-value{

        font-size:12px;

    }


    .stat-label{

        font-size:6px;

    }


    .hero h1{

        font-size:21px;

    }


    .box{

        padding:18px 13px;

    }

}

</style>

</head>

<body>


<!-- =====================================================
     LOGIN
====================================================== -->

<div
    class="login-box"
    id="loginBox"
>

    <div class="login-card">

        <div class="logo">
            RB
        </div>


        <h1>
            NAWWB KIING
        </h1>


        <div class="subtitle">
            SECURE CONTROL PANEL
        </div>


        <div class="input-group">

            <input
                type="text"
                id="username"
                placeholder="Username"
                autocomplete="username"
            >

        </div>


        <div class="input-group">

            <input
                type="password"
                id="password"
                placeholder="Password"
                autocomplete="current-password"
            >

        </div>


        <button
            class="login-btn"
            onclick="login()"
        >
            LOGIN TO PANEL
        </button>


        <div
            id="loginError"
            class="login-error"
        >
            Wrong username or password.
        </div>

    </div>

</div>


<!-- =====================================================
     MAIN PANEL
====================================================== -->

<div
    class="container"
    id="mainContent"
>


    <!-- NAV -->

    <nav class="navbar">

        <div class="brand">

            <div class="brand-icon"></div>

            <div class="brand-name">
                NAWAB KIING SYSTEM
            </div>

        </div>


        <div class="online">
            ● ONLINE
        </div>

    </nav>


    <!-- HERO -->

    <header class="hero">

        <h1>
            RAAJVEER BOSS
        </h1>

        <p>
            ADVANCED SOCIAL CONTROL PANEL
        </p>

    </header>


    <!-- STATS -->

    <section class="stats">

        <div class="stat">

            <div class="stat-value">
                READY
            </div>

            <div class="stat-label">
                SYSTEM
            </div>

        </div>


        <div class="stat">

            <div class="stat-value">
                24/7
            </div>

            <div class="stat-label">
                SERVICE
            </div>

        </div>


        <div class="stat">

            <div class="stat-value">
                LIVE
            </div>

            <div class="stat-label">
                STATUS
            </div>

        </div>

    </section>


    <!-- SERVICES -->

    <section class="services">


        <!-- FB POST -->

        <div class="box">

            <div class="card-icon">
                FB
            </div>

            <h2>
                FB POST COMMENTS
            </h2>

            <p>
                Post per automatic comments loader.
            </p>

            <a
                class="btn post-btn"
                href="http://127.0.0.1:5005"
            >
                OPEN FB POST SERVER
            </a>

        </div>


        <!-- FB CONVO -->

        <div class="box">

            <div class="card-icon">
                MSG
            </div>

            <h2>
                FB CONVO SERVER
            </h2>

            <p>
                Offline FB inbox/group messaging via token.
            </p>

            <a
                class="btn token-btn"
                href="http://127.0.0.1:5004/"
            >
                OPEN FB OFFLINE SERVER
            </a>

        </div>


        <!-- INSTAGRAM -->

        <div class="box">

            <div class="card-icon">
                IG
            </div>

            <h2>
                INSTAGRAM AUTO SPAMMER
            </h2>

            <p>
                Instagram DMs / Group spam loader.
            </p>

            <a
                class="btn combo-btn"
                href="https://in5t4gram-off.onrender.com"
                target="_blank"
                rel="noopener noreferrer"
            >
                OPEN IG LOADER
            </a>

        </div>


        <!-- WHATSAPP -->

        <div class="box">

            <div class="card-icon">
                WA
            </div>

            <h2>
                WHATSAPP OFFLINE SERVER
            </h2>

            <p>
                WhatsApp mobile/group spam offline loader.
            </p>

            <a
                class="btn whatsapp-btn"
                href="https://wa.me/"
                target="_blank"
                rel="noopener noreferrer"
            >
                OPEN WHATSAPP
            </a>

        </div>


        <!-- TELEGRAM -->

        <div class="box">

            <div class="card-icon">
                TG
            </div>

            <h2>
                TELEGRAM OFFLINE SERVER
            </h2>

            <p>
                Telegram group/inbox fight via offline server.
            </p>

            <a
                class="btn telegram-btn"
                href="https://t.me/"
                target="_blank"
                rel="noopener noreferrer"
            >
                OPEN TELEGRAM
            </a>

        </div>


        <!-- UPCOMING -->

        <div class="box">

            <div class="card-icon">
                ★
            </div>

            <h2>
                UPCOMING LOADER
            </h2>

            <p>
                Coming soon on 25 July.
            </p>

            <a
                class="btn instagram-btn"
                href="https://www.instagram.com/"
                target="_blank"
                rel="noopener noreferrer"
            >
                INSTAGRAM LAUNCH
            </a>

        </div>


    </section>


    <!-- FOOTER -->

    <footer class="footer">

        © 2026
        <span>
            RAAJVEER BOSS
        </span>

        • ADVANCED CONTROL PANEL

    </footer>

</div>


<!-- =====================================================
     JAVASCRIPT
====================================================== -->

<script>

/* =========================================================
   LOGIN
========================================================= */

function login(){

    const user =
        document.getElementById(
            'username'
        ).value.trim();

    const pass =
        document.getElementById(
            'password'
        ).value;

    const error =
        document.getElementById(
            'loginError'
        );


    /*
       Existing credentials preserved.
    */

    if(
        user === "admin" &&
        pass === "1234"
    ){

        document.getElementById(
            'loginBox'
        ).style.display = 'none';

        document.getElementById(
            'mainContent'
        ).style.display = 'block';

        document.body.style.overflow =
            'auto';

    }

    else{

        error.style.display =
            'block';

    }

}


/* =========================================================
   ENTER KEY LOGIN
========================================================= */

document
.getElementById('password')
.addEventListener(
    'keydown',
    function(event){

        if(event.key === 'Enter'){

            login();

        }

    }
);


/* =========================================================
   USERNAME ENTER
========================================================= */

document
.getElementById('username')
.addEventListener(
    'keydown',
    function(event){

        if(event.key === 'Enter'){

            document
            .getElementById('password')
            .focus();

        }

    }
);

</script>

</body>
</html>
'''

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
