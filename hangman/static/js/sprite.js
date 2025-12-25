function spriteController(idleSprite, baseUrl) {
    return {
        sprite: idleSprite,
        baseUrl: baseUrl,

        playSound(id){
            let audio = document.getElementById(id);
            audio.currentTime = 0;
            audio.play().catch(error => console.log("Audio playback error:", error));
        },

        playAnimation(action) {
            if (action === 'CORRECT') {
                setTimeout(() => {
                    this.sprite = baseUrl + 'wolf_hurt.gif';
                    this.playSound('snd-hit');
                }, 500);
                
                this.playSound('snd-correct');
            } else if (action === 'INCORRECT') {
                setTimeout(() => {
                    this.sprite = baseUrl + 'wolf_atk.gif';
                    this.playSound('snd-hit');
                }, 500);
                
                this.playSound('snd-incorrect');
            } else if (action === 'VICTORY') {
                setTimeout(() => {
                    this.sprite = baseUrl + 'wolf_death.gif';
                    this.playSound('snd-victory');
                }, 2000);

                setTimeout(() => {
                    this.playSound('snd-death');
                }, 1500);
                
                setTimeout(() => {
                    this.sprite = baseUrl + 'wolf_hurt.gif';
                    this.playSound('snd-hit');
                }, 500);

                this.playSound('snd-correct')
            } else if (action === 'DEFEAT') {
                setTimeout(() => {
                    this.sprite = baseUrl + 'wolf_idle.gif';
                    this.playSound('snd-defeat');
                }, 1000);
                
                this.playSound('snd-death');
            }

            if (action !== 'VICTORY') {
                setTimeout(() => {
                    this.sprite = baseUrl + 'wolf_idle.gif';
                }, 2000);
            }
        }
    }
}