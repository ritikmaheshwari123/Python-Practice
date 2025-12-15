import random
from num2words import num2words
import streamlit as st

# --- Data ---
teen_rhyme = [
    "You’re my queen 👑", "You’re my Valentine 💌", "You’re my sweet sexy teen 💖",
    "Would you love to prepare my tiffine 💌", "You’re my fantasy scene 😏",
    "Late-night thoughts getting mean 🔥", "You know exactly what I mean 😉",
    "Sweet on the surface, wild between 😈"
]

love_rhymes = {
    "zero": ["Zero doubts, I’m your hero 💘", "Zero clothes, just us tonight 😈", "Zero limits, hold me tight 🔥"],
    "one": ["From day one, our love begun ❤️", "You are the one, my forever one 💑",
            "Two souls dancing in one groove 💃🕺", "You’re the one I crave at night 😏",
            "One touch and I lose the fight 🔥"],
    "two": ["I love you ❤️", "Just us two, hearts so true 💞",
            "Two souls dancing in one groove 💃🕺", "Just us two, bodies in sync 😈",
            "Two drinks down, what do you think? 😉"],
    "three": ["With you, life feels free 😍", "Three words: I love you 💖", "After three, things get wild 😏"],
    "four": ["Tell me our love score 😘", "Loving you more and more 💖", "Four walls, just you and I 😏"],
    "five": ["You make me feel alive 🔥", "With you, my heart thrives 💘",
             "Five minutes alone, I’m undone 🔥", "High five? Or hands where they don’t belong 😈"],
    "six": ["Late night talks, whispers and tricks 😉", "Six senses wake when you're near 😏",
            "Six slow kisses, one by one 😘", "Six whispers saying ‘don’t stop’ 😏"],
    "seven": ["My heart to you is given ❤️", "With you, I’m in heaven ✨", "Seven sins, I want them all 😈"],
    "eight": ["You and mine same colgate 💞", "Together feels just great 💞", "You and I—perfect fate 😍",
              "Let’s stay up late, no sleep 😏", "Eight letters: ‘come to bed’ 😈"],
    "nine": ["You’re mine, and the stars align 🌟", "Nine times stronger, this love of mine 💘",
             "Nine times thinking of you tonight 🔥", "You’re my favorite kind of mine 😘"],
    "ten": ["If love was a game, we’d score a ten 💯", "Perfect match—again and again 😘",
            "Perfect ten, curves and grin 😏", "Ten out of ten, let the games begin 🔥"],
    "eleven": ["With you I have clear vision 🌟", "Past eleven, still thinking of you 😌",
               "Past eleven, clothes come off 😈", "Late hours make me soft… spoken 😉"],
    "twelve": ["My heart rings every time you tell 🔔", "Midnight love—twelve as well 💕",
               "Midnight strikes, you pull me close 🔥", "Twelve o’clock, we overdose 😈"],
    "teen": teen_rhyme,
    "ty": ["Feeling naughty but sweet-y 😏", "Come closer, talk to me 💋",
           "Getting naughty, slightly dirty 😏", "Come talk close, real flirty 😈"],
    "hundred": ["Hundred reasons I want you 💖", "Love you times a hundred 💘",
                "A hundred ways to tease you slow 🔥", "A hundred sparks, let them flow 😏"],
    "thousand": ["A thousand kisses overdue 😘", "I’d cross a thousand miles for you 💑",
                 "A thousand thoughts I won’t text 😈", "A thousand kisses… what’s next? 🔥"],
    "million": ["Million sparks when you’re near 🔥"]
}


# --- Functions ---
def get_rhyme(last_rhyme):
    if last_rhyme in love_rhymes:
        return random.choice(love_rhymes[last_rhyme])
    if last_rhyme.endswith("teen"):
        return random.choice(love_rhymes["teen"])
    if last_rhyme.endswith("ty"):
        return random.choice(love_rhymes["ty"])
    if last_rhyme.endswith("hundred"):
        return random.choice(love_rhymes["hundred"])
    if last_rhyme.endswith("thousand"):
        return random.choice(love_rhymes["thousand"])
    if last_rhyme.endswith("million"):
        return random.choice(love_rhymes["million"])
    return "My love cannot be decided by this program baby 😜"


def calculate(expression):
    try:
        if '+' in expression:
            a, b = expression.split('+')
            result = int(a.strip()) + int(b.strip())
        elif '-' in expression:
            a, b = expression.split('-')
            result = int(a.strip()) - int(b.strip())
        elif '*' in expression:
            a, b = expression.split('*')
            result = int(a.strip()) * int(b.strip())
        elif '/' in expression:
            a, b = expression.split('/')
            b = int(b.strip())
            if b == 0:
                return None, "💔 Division by zero gives infinity, which is my love for you baby 😘"
            result = int(int(a.strip()) / b)
        else:
            return None, "❌ Choose operator from +  -  *  / only 😜"
        return result, None
    except:
        return None, "❌ Please enter a valid expression like: 3 + 4 😘"


# --- Streamlit UI ---
st.set_page_config(page_title="💘 Love Calculator 💘", page_icon="💖", layout="centered")

# --- CSS & Heart Animation ---
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #fbc2eb, #a6c1ee);
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.stButton>button {
    background: hotpink;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 18px;
}
.card {
    background: rgba(255,255,255,0.2);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
    backdrop-filter: blur( 8px );
    margin-top: 20px;
}
.flirt-meter {
    height: 20px;
    background: pink;
    border-radius: 10px;
    margin: 10px 0px;
}
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-30px);}
    100% {transform: translateY(0px);}
}
.heart {
    position: absolute;
    font-size: 24px;
    animation: float 2s infinite;
}
</style>
<script>
function createHearts() {
    for (let i = 0; i < 30; i++) {
        let heart = document.createElement("div");
        heart.className = "heart";
        heart.style.left = Math.random() * window.innerWidth + "px";
        heart.style.top = Math.random() * window.innerHeight + "px";
        heart.innerHTML = "💖";
        document.body.appendChild(heart);
    }
}
window.onload = createHearts;
</script>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#ff66cc;'>💘 Love Rhyme Calculator 💘</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ff99cc;'>Calculate numbers & get a love rhyme 💌</p>",
            unsafe_allow_html=True)

# --- Input Card ---
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    expression = st.text_input("Enter calculation (e.g. 4 + 5, 10 - 2, 6 * 3, 8 / 2):")

    if st.button("💖 Calculate and get love rhyme 💖"):
        result, error = calculate(expression)
        if error:
            st.error(error)
        else:
            # st.success(f"🧮 Result: {result}")

            # Show full number word
            word = num2words(int(result)).replace("-", " ")
            st.success(f"📝 Result: {word}")  # <-- Full word display

            # Flirt Meter
            flirt_level = 100
            st.markdown(
                f'<div class="flirt-meter" style="width:{flirt_level}%; background:linear-gradient(90deg, #ff66cc, #ffccff);"></div>',
                unsafe_allow_html=True)

            word = num2words(int(result)).replace("-", " ").lower()
            last_word = word.split()[-1]
            rhyme = get_rhyme(last_word)
            st.balloons()
            st.markdown(f"<h3 style='color:#ff3399;'>💌 {rhyme}</h3>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
