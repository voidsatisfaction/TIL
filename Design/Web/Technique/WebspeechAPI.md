## Sources

- [Web Speech API - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

## Explanation

웹 어플리케이션에서 음성을 합성할 수 있게 하는 기술이다.

음성을 감지하는 기능 + 음성을 내보내는 기능을 가지고 있다.

신기하게도 음성을 내보내는 기능은 문자만 봐도 그대로 음성을 내보내준다.

IE에서는 지원되지 않는다.

## Code

```js
// Utterance speech setting
function speechSetup() {
  const synthes = new SpeechSynthesisUtterance()
  synthes.lang = "ko-KO"

  console.log('say: ' + '당신은 낚였습니다.')
  synthes.text = "당신은 낚였습니다.... 아줌마 바보 멍청이."
  speechSynthesis.speak(synthes);
}

// Execution
speechSetup();

```