# 🔥 TIL: JavaScript

>   *   **updated on:** 2021-11-07  23:48
>   *   **written by:** Sanghyun Park



#### 📌 References

>   1.   **[cross browser issue](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction#why_do_cross_browser_issues_occur)**
>   1.   XSS(Cross-site Scripting)



#### 📚 Contents

>   1.   DOM
>        1.   DOM manipulation
>        2.   Event



<br>

## 001. DOM(Document Object Model)

>   HTML, XML 등과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스



##### 👉 Notes. window

>   DOM을 표현하는 창 즉, 브라우저 창으로서 가장 최상위의 객체이다.



##### 👉 Notes. BOM(Browser Object Model)

>   JavaScript가 브라우저와 소통하고 브라우저를 프로그래밍적으로 제어할 수 있는 수단을 제공하는 모델
>
>   *   ```javascript
>       // browser 탭 열기
>       window.open()
>       
>       // browser 화면 인쇄창 열기
>       window.print()
>       
>       // 확인과 취소 버튼이 있는 모달 창 호출하기
>       window.confirm()
>       ```



### 001.1. DOM manipulation

>   DOM 조작은 먼저 **(1) 선택**을 한 후에 **(2) 조작**을 하는 흐름이다.



#### A. DOM 관련 객체의 상속 구조

>   1.   EventTarget
>   2.   Node
>   3.   Element / Document
>   4.   HTMLElement



#### B. DOM 선택

>   ```javascript
>   // CSS selector에 부합하는 첫 번째 element 선택(존재하지 않으면, null 반환)
>   document.querySelector('selector')
>   
>   // CSS selector에 부합하는 모든 element를 선택하여 NodeList를 반환
>   document.querySelectorAll('selector')
>   
>   // 그 외
>   document.getElementById('id selector')
>   document.getElementsByTagName('tag selector')  // HTMLCollection 반환
>   document.getElementsByClassName('class selector')  // HTMLCollection 반환
>   
>   // 선택한 element의 해당 속성값(문자열) 반환
>   element.getAttribute('attribute name')
>   ```



##### 👉 Notes. HTMLCollection vs. NodeList

>   HTMLCollection과 NodeList 모두 index로 접근 가능한 유사 배열이며, **live collection**(DOM 변경사항 실시간 반영)이다.
>
>   *   HTMLCollection
>       *   index를 포함하여 name과 id로 각 원소에 접근 가능
>   *   NodeList
>       *   index로만 각 원소에 접근 가능
>       *   array에서 사용 가능한 메서드 사용 가능
>       *   `querySelectorAll()`에 의해 반환된 NodeList는 **static collection**의 성질을 띔



#### C. DOM 생성 및 추가

>   ```javascript
>   // 인자로 넘겨준 tag name의 tag 생성
>   document.createElement('tag name')
>   
>   // 마지막에 여러 Node 객체 혹은 DOMString을 추가할 수 있으며, 반환값이 없음
>   element.append(Node or DOMString)
>   
>   // 마지막에 하나의 Node 객체만을 추가하며, 추가된 Node 객체를 반환함
>   element.appendChild(Node)
>   ```



#### D. DOM 변경

>   ```javascript
>   // 선택한 element 내의 raw text
>   element.innerText
>   
>   // 선택한 element 내의 HTML markup(XSS 공격에 취약하므로 사용 시 주의 필요)
>   element.innerHTML
>   
>   // 선택한 element에 속성과 해당 속성의 값 설정(이미 존재하는 속성일 경우, 값이 갱신됨)
>   element.setAttribute('attribute name', 'attribute value')
>   ```



#### E. DOM 삭제

>   ```javascript
>   // 선택한 element 삭제
>   element.remove()
>   
>   // 선택한 element의 특정 자식 element 삭제하고, 삭제된 element 반환
>   element.removeChild()
>   ```



<br>

## 002. Event

>   사용자와의 상호작용과 같은 사건의 발생을 전달하기 위한 객체



### 002.1. Event

>   Event를 작성하는 것은 "관련 element에 특정 event가 **발생**했을 때의 할 일을 **등록**하는 것"이다.



#### A. Event Handler

>   ```javascript
>   // 관련 element에 event 등록하기
>   element.addEventListener('event type', listener)  // listener: event가 발생했을 때 알림을 받는 객체
>   ```



#### B. Event 취소

>   ```javascript
>   // 해당 이벤트의 전파를 막지 않은 채, 기본 동작을 취소시킴(event.cancelable이 false인 경우, 취소 불가)
>   event.preventDefault()
>   ```

