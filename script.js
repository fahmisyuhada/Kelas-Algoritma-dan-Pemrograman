document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fireworks = new Fireworks({
        target: document.body,
        hue: { min: 0, max: 360 },
        delay: { min: 15, max: 30 },
        speed: 2,
        acceleration: 1.05,
        friction: 0.97,
        gravity: 1.5,
        particles: 50,
        trace: 3,
        explosion: 5,
        autoresize: true,
        brightness: { min: 50, max: 80, decay: { min: 0.015, max: 0.03 } },
        boundaries: { top: 50, bottom: document.documentElement.clientHeight, left: 50, right: document.documentElement.clientWidth },
        sound: {
            enable: true,
            list: ['explosion0.mp3', 'explosion1.mp3', 'explosion2.mp3'],
            min: 4,
            max: 8
        }
    });

    fireworks.start();

    setTimeout(() => {
        fireworks.stop();
    }, 5000);
});
