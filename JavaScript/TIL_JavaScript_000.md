# ๐ฅ TIL: JavaScript

>   *   **updated on:** 2021-11-07  23:48
>   *   **written by:** Sanghyun Park



#### ๐ References

>   1.   **[cross browser issue](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction#why_do_cross_browser_issues_occur)**
>   1.   XSS(Cross-site Scripting)



#### ๐ Contents

>   1.   DOM
>        1.   DOM manipulation
>        2.   Event



<br>

## 001. DOM(Document Object Model)

>   HTML, XML ๋ฑ๊ณผ ๊ฐ์ ๋ฌธ์๋ฅผ ๋ค๋ฃจ๊ธฐ ์ํ ๋ฌธ์ ํ๋ก๊ทธ๋๋ฐ ์ธํฐํ์ด์ค



##### ๐ Notes. window

>   DOM์ ํํํ๋ ์ฐฝ ์ฆ, ๋ธ๋ผ์ฐ์  ์ฐฝ์ผ๋ก์ ๊ฐ์ฅ ์ต์์์ ๊ฐ์ฒด์ด๋ค.



##### ๐ Notes. BOM(Browser Object Model)

>   JavaScript๊ฐ ๋ธ๋ผ์ฐ์ ์ ์ํตํ๊ณ  ๋ธ๋ผ์ฐ์ ๋ฅผ ํ๋ก๊ทธ๋๋ฐ์ ์ผ๋ก ์ ์ดํ  ์ ์๋ ์๋จ์ ์ ๊ณตํ๋ ๋ชจ๋ธ
>
>   *   ```javascript
>       // browser ํญ ์ด๊ธฐ
>       window.open()
>       
>       // browser ํ๋ฉด ์ธ์์ฐฝ ์ด๊ธฐ
>       window.print()
>       
>       // ํ์ธ๊ณผ ์ทจ์ ๋ฒํผ์ด ์๋ ๋ชจ๋ฌ ์ฐฝ ํธ์ถํ๊ธฐ
>       window.confirm()
>       ```



### 001.1. DOM manipulation

>   DOM ์กฐ์์ ๋จผ์  **(1) ์ ํ**์ ํ ํ์ **(2) ์กฐ์**์ ํ๋ ํ๋ฆ์ด๋ค.



#### A. DOM ๊ด๋ จ ๊ฐ์ฒด์ ์์ ๊ตฌ์กฐ

>   1.   EventTarget
>   2.   Node
>   3.   Element / Document
>   4.   HTMLElement



#### B. DOM ์ ํ

>   ```javascript
>   // CSS selector์ ๋ถํฉํ๋ ์ฒซ ๋ฒ์งธ element ์ ํ(์กด์ฌํ์ง ์์ผ๋ฉด, null ๋ฐํ)
>   document.querySelector('selector')
>   
>   // CSS selector์ ๋ถํฉํ๋ ๋ชจ๋  element๋ฅผ ์ ํํ์ฌ NodeList๋ฅผ ๋ฐํ
>   document.querySelectorAll('selector')
>   
>   // ๊ทธ ์ธ
>   document.getElementById('id selector')
>   document.getElementsByTagName('tag selector')  // HTMLCollection ๋ฐํ
>   document.getElementsByClassName('class selector')  // HTMLCollection ๋ฐํ
>   
>   // ์ ํํ element์ ํด๋น ์์ฑ๊ฐ(๋ฌธ์์ด) ๋ฐํ
>   element.getAttribute('attribute name')
>   ```



##### ๐ Notes. HTMLCollection vs. NodeList

>   HTMLCollection๊ณผ NodeList ๋ชจ๋ index๋ก ์ ๊ทผ ๊ฐ๋ฅํ ์ ์ฌ ๋ฐฐ์ด์ด๋ฉฐ, **live collection**(DOM ๋ณ๊ฒฝ์ฌํญ ์ค์๊ฐ ๋ฐ์)์ด๋ค.
>
>   *   HTMLCollection
>       *   index๋ฅผ ํฌํจํ์ฌ name๊ณผ id๋ก ๊ฐ ์์์ ์ ๊ทผ ๊ฐ๋ฅ
>   *   NodeList
>       *   index๋ก๋ง ๊ฐ ์์์ ์ ๊ทผ ๊ฐ๋ฅ
>       *   array์์ ์ฌ์ฉ ๊ฐ๋ฅํ ๋ฉ์๋ ์ฌ์ฉ ๊ฐ๋ฅ
>       *   `querySelectorAll()`์ ์ํด ๋ฐํ๋ NodeList๋ **static collection**์ ์ฑ์ง์ ๋



#### C. DOM ์์ฑ ๋ฐ ์ถ๊ฐ

>   ```javascript
>   // ์ธ์๋ก ๋๊ฒจ์ค tag name์ tag ์์ฑ
>   document.createElement('tag name')
>   
>   // ๋ง์ง๋ง์ ์ฌ๋ฌ Node ๊ฐ์ฒด ํน์ DOMString์ ์ถ๊ฐํ  ์ ์์ผ๋ฉฐ, ๋ฐํ๊ฐ์ด ์์
>   element.append(Node or DOMString)
>   
>   // ๋ง์ง๋ง์ ํ๋์ Node ๊ฐ์ฒด๋ง์ ์ถ๊ฐํ๋ฉฐ, ์ถ๊ฐ๋ Node ๊ฐ์ฒด๋ฅผ ๋ฐํํจ
>   element.appendChild(Node)
>   ```



#### D. DOM ๋ณ๊ฒฝ

>   ```javascript
>   // ์ ํํ element ๋ด์ raw text
>   element.innerText
>   
>   // ์ ํํ element ๋ด์ HTML markup(XSS ๊ณต๊ฒฉ์ ์ทจ์ฝํ๋ฏ๋ก ์ฌ์ฉ ์ ์ฃผ์ ํ์)
>   element.innerHTML
>   
>   // ์ ํํ element์ ์์ฑ๊ณผ ํด๋น ์์ฑ์ ๊ฐ ์ค์ (์ด๋ฏธ ์กด์ฌํ๋ ์์ฑ์ผ ๊ฒฝ์ฐ, ๊ฐ์ด ๊ฐฑ์ ๋จ)
>   element.setAttribute('attribute name', 'attribute value')
>   ```



#### E. DOM ์ญ์ 

>   ```javascript
>   // ์ ํํ element ์ญ์ 
>   element.remove()
>   
>   // ์ ํํ element์ ํน์  ์์ element ์ญ์ ํ๊ณ , ์ญ์ ๋ element ๋ฐํ
>   element.removeChild()
>   ```



<br>

## 002. Event

>   ์ฌ์ฉ์์์ ์ํธ์์ฉ๊ณผ ๊ฐ์ ์ฌ๊ฑด์ ๋ฐ์์ ์ ๋ฌํ๊ธฐ ์ํ ๊ฐ์ฒด



### 002.1. Event

>   Event๋ฅผ ์์ฑํ๋ ๊ฒ์ "๊ด๋ จ element์ ํน์  event๊ฐ **๋ฐ์**ํ์ ๋์ ํ  ์ผ์ **๋ฑ๋ก**ํ๋ ๊ฒ"์ด๋ค.



#### A. Event Handler

>   ```javascript
>   // ๊ด๋ จ element์ event ๋ฑ๋กํ๊ธฐ
>   element.addEventListener('event type', listener)  // listener: event๊ฐ ๋ฐ์ํ์ ๋ ์๋ฆผ์ ๋ฐ๋ ๊ฐ์ฒด
>   ```



#### B. Event ์ทจ์

>   ```javascript
>   // ํด๋น ์ด๋ฒคํธ์ ์ ํ๋ฅผ ๋ง์ง ์์ ์ฑ, ๊ธฐ๋ณธ ๋์์ ์ทจ์์ํด(event.cancelable์ด false์ธ ๊ฒฝ์ฐ, ์ทจ์ ๋ถ๊ฐ)
>   event.preventDefault()
>   ```

