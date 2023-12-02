<style>
@keyframes snowflakes {
    0% { top: -10px; left: calc(random() * 100%); opacity: 0.5; }
    100% { top: 100vh; left: calc(random() * 100%); opacity: 0.5; }
}
/* Randomize animation duration for each snowflake */
@keyframes randomize-duration {
    0% { --random-duration: 0s; left: calc(random() * 100%); }
    100% { --random-duration: calc(20s + var(--random-duration)); top: 100vh; left: calc(random() * 100%); }
}

html, body {
    height: 100%;
    margin: 0;
    overflow: hidden;
}

div {
    position: relative;
}

span {
    position: relative;
    animation: snowflakes 20s linear infinite;
    left: calc(random() * 100%);
    opacity: 0.5;
}

/* Apply randomize-duration animation to each snowflake */
span {
    animation: snowflakes 20s linear infinite, randomize-duration;
    left: calc(random() * 100%);
}
.snowflake1 {
    animation: snowflakes 8s linear infinite;
    animation-delay: 0.5s;
}
.snowflake2 {
    animation: snowflakes 6.3s linear infinite;
    animation-delay: 0s;
}
.snowflake3 {
    animation: snowflakes 5s linear infinite;
    animation-delay: 3s;
}
.snowflake4 {
    animation: snowflakes 5.5s linear infinite;
    animation-delay: 2s;
}
.snowflake5 {
    animation: snowflakes 7s linear infinite;
    animation-delay: 3s;
}
.snowflake6 {
    animation: snowflakes 6s linear infinite;
    animation-delay: 1s;
}
.snowflake7 {
    animation: snowflakes 5.7s linear infinite;
    animation-delay: 2s;
}
.snowflake8 {
    animation: snowflakes 7.4s linear infinite;
    animation-delay: 0.3s;
}
.snowflake9 {
    animation: snowflakes 4.5s linear infinite;
    animation-delay: 0s;
}
</style>
<div>
    <span class="snowflake1">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake3">❄️</span>
    <span class="snowflake4">❄️</span>
    <span class="snowflake5">❄️</span>
    <span class="snowflake6">❄️</span>
    <span class="snowflake1">❄️</span>
    <span class="snowflake4">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake7">❄️</span>
    <span class="snowflake4">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake9">❄️</span>
    <span class="snowflake1">❄️</span>
    <span class="snowflake6">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake9">❄️</span>
    <span class="snowflake5">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake6">❄️</span>
    <span class="snowflake9">❄️</span>
    <span class="snowflake7">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake1">❄️</span>
    <span class="snowflake4">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake6">❄️</span>
    <span class="snowflake1">❄️</span>
    <span class="snowflake9">❄️</span>
    <span class="snowflake3">❄️</span>
    <span class="snowflake7">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake9">❄️</span>
    <span class="snowflake1">❄️</span>
    <span class="snowflake4">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake1">❄️</span>
    <span class="snowflake8">❄️</span>
    <span class="snowflake2">❄️</span>
    <span class="snowflake6">❄️</span>
    <span class="snowflake1">❄️</span>
</div>

# 🎄 Pim's adventofcode solutions 🎅

Welcome to the magical world of Christmas! 🎉✨

## 🌟 Goal of this repo

I plan to complete as many puzzles of the adventofcode calendar as possible! I'm looking forward to work on these puzzles and I'm sure I'll learn a lot, you can find my solutions in this repo!


<style>
</style>
</div>
