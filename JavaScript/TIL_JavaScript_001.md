# ๐ฅ TIL: JavaScript

>   *   **updated on:** 2021-11-07  23:03
>   *   **written by:** Sanghyun Park



#### ๐ References

>   1.   **[Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)**
>   2.   **[typeof null](https://2ality.com/2013/10/typeof-null.html)**
>   2.   **[methods of Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)**



#### ๐ Contents

>   1.   ECMAScript6
>        1.   ๋ณ์์ ์๋ณ์
>        2.   ํ์๊ณผ ์ฐ์ฐ์
>        3.   ์กฐ๊ฑด๋ฌธ๊ณผ ๋ฐ๋ณต๋ฌธ
>        3.   ํจ์
>        3.   ๋ฐฐ์ด๊ณผ ๊ฐ์ฒด



<br>

## 1. ECMAScript 6

>   ECMA์์ ECMA-262 ๊ท๊ฒฉ์ ๋ฐ๋ผ ์ ์ํ, ํ์คํ๋ JavaScript



##### ๐ Note

>   JavaScript๋ ASI(Automatic Semicolon Insertion)์ ์ํด semicolon์ด ์๋์ผ๋ก ์ฝ์๋จ(์ ํ์  ์ฌ์ฉ ๊ฐ๋ฅ)



### 1.1. ๋ณ์์ ์๋ณ์



#### A. ์๋ณ์ ๊ท์น

>   1.   ๋ฌธ์, dollar, underscore๋ก ์์
>   2.   ๋์๋ฌธ์ ๊ตฌ๋ถ
>        1.   **camelCase**(lower-camel-case): ๋ณ์, ํจ์, ๊ฐ์ฒด
>        2.   **PascalCase**(upper-camel-case): ํด๋์ค(์์ฑ์)
>        3.   **SNAKE_CASE**: ์์
>   3.   ์์ฝ์ด ์ฌ์ฉ ๋ถ๊ฐ



#### B. ๋ณ์ ์ ์ธ ํค์๋

>   1.   **let:** ์ฌ์ ์ธ ๋ถ๊ฐ๋ฅ, ์ฌํ ๋น ๊ฐ๋ฅ, ๋ธ๋ก ์ค์ฝํ
>   2.   **const:** ์ฌ์ ์ธ ๋ถ๊ฐ๋ฅ, ์ฌํ ๋น ๋ถ๊ฐ๋ฅ, ๋ธ๋ก ์ค์ฝํ
>   3.   **var:** ์ฌ์ ์ธ ๊ฐ๋ฅ, ์ฌํ ๋น ๊ฐ๋ฅ, ํจ์ ์ค์ฝํ, hoisting ๋ฐ์
>        *   **hoisting:** ๋ณ์๊ฐ ์ ์ธ๋ ์์น๋ณด๋ค ์์์ ํด๋น ๋ณ์๊ฐ ์ฐธ์กฐ๋๋ ํ์(undefined ๋ฐํ)



##### ๐ Note

>   *   **๋ธ๋ก ์ค์ฝํ**๋ if๋ฌธ, for๋ฌธ, ํจ์ ๋ฑ์ ์ค๊ดํธ({}) ๋ด๋ถ๋ฅผ ์ง์นญํ๋ ๊ฐ๋์ผ๋ก ํน์  ๋ธ๋ก ๋ด ๋ณ์๋ ํด๋น ๋ธ๋ก์ ์ธ๋ถ์์ ์ ๊ทผํ  ์ ์์
>   *   **ํจ์ ์ค์ฝํ**๋ ํจ์์ ์ค๊ดํธ({}) ๋ด๋ถ๋ฅผ ์ง์นญํ๋ ๊ฐ๋์ผ๋ก ํน์  ํจ์ ๋ด ๋ณ์๋ ํจ์ ๋ฐ๊นฅ์์ ์ ๊ทผํ  ์ ์์



<br>

### 1.2. ๋ฐ์ดํฐ ํ์๊ณผ ์ฐ์ฐ์



#### A. ๋ฐ์ดํฐ ํ์

>   1.   **Primitive Type:** ๋ณ์์ ํด๋น ํ์์ ์ค์  ๊ฐ์ด ์ ์ฅ๋จ, ๋ค๋ฅธ ๋ณ์๋ก ๋ณต์ฌํ  ๋ ํด๋น ๊ฐ์ด ๋ณต์ฌ๋จ
>
>        1.   **Number**
>
>             *   NaN(Not-a-Number): ๊ณ์ฐ ๋ถ๊ฐ๋ฅํ ๊ฒฝ์ฐ์ ๋ฐํ๋๋ ๊ฐ
>
>        2.   **String**
>
>             *   Template Literal: backtick์ผ๋ก ๊ฐ์ธ์ง ๋ฌธ์์ด์ `${expression}`์ ํ์ฉํ์ฌ ํํ์์ ์ฝ์ํ  ์ ์์
>
>        3.   **Boolean**
>
>             *   ToBoolean Conversion
>                 *   true: Object
>                 *   false: Undefined, Null, Number(0, -0, NaN), String(๋น ๋ฌธ์์ด)
>
>        4.   **Undefined**
>
>        5.   **Null**
>
>             *   In JavaScript, `typeof null` is `'object'`, which incorrectly suggests that `null` is an object (it isnโt, itโs a primitive value, consult my blog post on [categorizing values](http://2ality.com/2013/01/categorizing-values.html) for details). This is a bug and one that unfortunately canโt be fixed, because it would break existing code.
>
>             
>
>   2.   **Reference Type:** ๋ณ์์ ํด๋น ๊ฐ์ฒด์ ์ฐธ์กฐ ๊ฐ์ด ์ ์ฅ๋จ, ๋ค๋ฅธ ๋ณ์๋ก ๋ณต์ฌํ  ๋ ํด๋น ๊ฐ์ฒด์ ์ฐธ์กฐ ๊ฐ์ด ๋ณต์ฌ๋จ



##### ๐ Note

>   **typeof:** ํด๋น ๋ณ์์ ๋ฐ์ดํฐ ํ์์ ํ์ธํ๊ธฐ ์ํ ์ฐ์ฐ์



##### ๐ Note

>   *   ์ซ์ํ ๋ฐ์ดํฐ์ ๋ฌธ์์ด ๋ฐ์ดํฐ์ ๋ํด ๋ํ๊ธฐ(Number + String) ์ฐ์ฐ์ ์ํํ๋ฉด ์ซ์ํ ๋ฐ์ดํฐ๊ฐ ๋ฌธ์์ด ๋ฐ์ดํฐ๋ก ํ๋ณํ๋ ํ concatenation์ด ์ํ๋จ
>   *   ์ซ์ํ ๋ฐ์ดํฐ์ ๋ถ๋ฆฌ์ธ ๋ฐ์ดํฐ์ ๋ํด ๋ํ๊ธฐ(Number + Boolean) ์ฐ์ฐ์ ์ํํ๋ฉด ๋ถ๋ฆฌ์ธ ๋ฐ์ดํฐ๊ฐ ์ซ์ํ ๋ฐ์ดํฐ๋ก ํ๋ณํ๋ ํ ์ฐ์ ์ฐ์ฐ์ด ์ํ๋จ



#### B. ์ฐ์ฐ์

>   1.   **ํ ๋น ์ฐ์ฐ์(`=`)**
>        1.   Increment ์ฐ์ฐ์(`variable++)`: ํผ์ฐ์ฐ์์ ๊ฐ์ 1 ์ฆ๊ฐ์ํด
>        2.   Decrement ์ฐ์ฐ์(`variable--)`: ํผ์ฐ์ฐ์์ ๊ฐ์ 1 ๊ฐ์์ํด
>   2.   **๋น๊ต ์ฐ์ฐ์**
>        *   ์ํ๋ฒณ ๋น๊ต๋ ์ฌ์  ์์์ ํ ์์์ผ์๋ก ํฐ ๊ฐ์ผ๋ก ํ๊ฐ๋๋ฉฐ, ์๋ฌธ์๊ฐ ๋๋ฌธ์๋ณด๋ค ๋ ํฌ๋ค๊ณ  ํ์ ๋จ
>   3.   **๋๋ฑ ๋น๊ต ์ฐ์ฐ์(`==`)**
>        *   ์๋ฌต์  ํ์ ๋ณํ์ ์ํํ์ฌ ๋น๊ต ๋์๋ค์ ํ์์ ์ผ์น์ํจ ํ ์๋ก ๊ฐ์ ๊ฐ์ธ์ง ํ๊ฐ
>   4.   **์ผ์น ๋น๊ต ์ฐ์ฐ์(`===`)**
>        *   ์๊ฒฉํ ๋น๊ต ์ฆ, ๋น๊ต ๋์๋ค์ ๋ฐ์ดํฐ ํ์๊ณผ ๊ฐ์ ๋ชจ๋ ๋น๊ตํ์ฌ ์๋ก ๊ฐ์ ๊ฐ์ธ์ง ํ๊ฐ
>   5.   **๋ผ๋ฆฌ ์ฐ์ฐ์(๋จ์ถ ํ๊ฐ ์ง์)**
>        *   and: &&
>        *   or: ||
>        *   not: !
>   6.   **Ternary Operator**(`expression ? value_when_true : value_when_false`)



<br>

### 1.3. ์กฐ๊ฑด๋ฌธ๊ณผ ๋ฐ๋ณต๋ฌธ



#### A. ์กฐ๊ฑด๋ฌธ

>   1.   **if statement**
>
>        *   ```javascript
>            if (condition) {
>                console.log('Hello JavaScript :)')
>            } else if (condition) {
>                console.log('I\'m Sanghyun Park!')
>            } else {
>                console.log('Nice to meet you.')
>            }
>            ```



>   2.   **switch statement**
>
>        *   ```javascript
>            switch(expression) {
>                case value_1: {
>            	    console.log('Hello JavaScript :)')
>                    break  // break๊ฐ ์๋ ๊ฒฝ์ฐ, ๋ค์ case๋ก fall-through๊ฐ ๋จ
>                }
>                case value_2: {
>                    console.log('I\'m Sanghyun Park!')
>                    break
>                }
>                default: {
>            	    console.log('Nice to meet you.')
>                }
>            }
>            ```



#### B. ๋ฐ๋ณต๋ฌธ

>   1.   **while**
>
>        *   ```javascript
>            while (condition) {
>                console.log('Hello JavaScript :)')
>            }
>            ```



>   2.   **for**
>
>        1.  **for**
>
>            *   ```javascript
>                for (initialization; condition; expression) {
>                    console.log('Hello JavaScript :)')
>                }
>                ```
>        
>        2.  **for in**
>        
>            *   ```javascript
>                for (attribute in object) {
>                    console.log(attribute)  // object์ attribute(key: value)๋ฅผ ์ํํ๋ฉฐ ์ถ๋ ฅํ๋ฉด key๊ฐ ์ถ๋ ฅ๋จ
>                }
>                ```
>        
>        3.  **for of**
>        
>            *   ์ํ ๊ฐ๋ฅํ ๊ฐ์ฒด์ ์ฌ์ฉ ๊ฐ๋ฅ
>        
>                *   string, array, set, map
>                *   object๋ ์ํ ๊ฐ๋ฅํ ๊ฐ์ฒด๊ฐ ์๋(Uncaught TypeError ๋ฐ์)
>        
>            *   ```javascript
>                for (element of iterables) {
>                    console.log(element)
>                }
>                ```



<br>

### 1.4. ํจ์



##### ๐ Note

>   *   JavaScript์ ํจ์๋ First-class object์ ํด๋นํ๋ฏ๋ก, (1) ๋ณ์์ ํ ๋น ๊ฐ๋ฅํ๊ณ , (2) ๋งค๊ฐ๋ณ์๋ก ์ ๋ฌ๋  ์ ์์ผ๋ฉฐ, ๋ํ (3) ๋ฐํ๊ฐ์ผ๋ก ์ ๋ฌ ๋ฐ์ ์ ์์



#### A. function statement

>   1.   **Function Declaration**
>
>        *   hoisting์ด ๋ฐ์ํ  ์ ์์
>
>        *   ```javascript
>            function func_name(args) {
>                console.log(args)
>            }
>            ```
>
>   2.   **Function Expression**
>
>        *   hoisting์ด ๋ฐ์ํ์ง ์์
>            *   var keyword๋ก function expression์ ์์ฑํ ๊ฒฝ์ฐ, ํด๋น ๋ณ์๋ ์ ์ธ ์ ์ undefined๋ก ์ด๊ธฐํ๋์ด Uncaught TypeError ๋ฐ์
>
>        *   ```javascript
>            const variable = function (arg = default_value) {  // default argument
>                console.log(args)
>            }
>            ```



#### B. Arrow Function

>   1.   ์ถ์ฝ ๊ณผ์ 
>
>        *   ```javascript
>            // step 0. function expression
>            const variable = function (args) {
>                return args * 2
>            }
>                              
>            // step 1. function keyword ์๋ต
>            const variable = (args) => {
>                return args * 2
>            }
>                              
>            // step 2. ๋งค๊ฐ ๋ณ์์ ๊ฐ์๊ฐ ํ ๊ฐ์ผ ๋, ์๊ดํธ ์๋ต
>            const variable = args => {
>                return args * 2
>            }
>                              
>            // step 3. ํจ์ body์ ํํ์์ด ํ ๊ฐ์ผ ๋, return keyword์ ์ค๊ดํธ ์๋ต
>            const variable = args => args * 2
>            ```



<br>

### 1.5. ๋ฐฐ์ด๊ณผ ๊ฐ์ฒด

>   **๋ฐฐ์ด**
>
>   *   ์์์ ์์๊ฐ ๋ณด์ฅ๋จ
>   *   0๊ณผ ์์ ์ ์๋ก ์ธ๋ฑ์ฑ ๊ฐ๋ฅ
>   *   ์์ ์ ์๋ก๋ ์ธ๋ฑ์ฑ ๋ถ๊ฐ(undefined ๋ฐํ)



>   **๊ฐ์ฒด**
>
>   *   key๋ ๋ฌธ์์ด ํ์๋ง ๊ฐ๋ฅ
>       *   key๊ฐ ํ ๋จ์ด๋ก ๊ตฌ์ฑ๋ ๊ฒฝ์ฐ ๋ฐ์ดํ๋ฅผ ์ฌ์ฉํ์ง ์์๋ ๋จ
>   *   value๋ ๋ชจ๋  ํ์์ด ๊ฐ๋ฅ
>   *   ๊ฐ์ฒด์ ์์ฑ(property)์ dot(`.`) ํน์ ๋๊ดํธ๋ก ์ ๊ทผ ๊ฐ๋ฅ
>       *   key์ ๊ตฌ๋ถ์๊ฐ ์ํด ์์ผ๋ฉด, ํด๋น key์ value๋ ๋๊ด๋ก๋ก ์ ๊ทผํด์ผ ํจ



#### A. Array Methods

>   1.   **.reverse()**
>   2.   **.push(element) & .pop()**
>   3.   **.unshift(element) & .shift()**
>   4.   **.includes()**
>   5.   **.indexOf()**
>        *   ํด๋น ๋ฐฐ์ด์ ์ฐพ๊ณ ์ ํ๋ ์์๊ฐ ์ฌ๋ฌ ๊ฐ ์กด์ฌํ๋ ๊ฒฝ์ฐ, ๊ฐ์ฅ ์์  ์ธ๋ฑ์ค ๋ฐํ
>        *   ํด๋น ๋ฐฐ์ด์ ์ฐพ๊ณ ์ ํ๋ ์์๊ฐ ์กด์ฌํ์ง ์๋ ๊ฒฝ์ฐ, **-1** ๋ฐํ
>   6.   **.join(separator=',')**



##### ๐ Note

>   *   callback function
>       *   ์ด๋ค ํจ์ ๋ด๋ถ์์ ์คํ๋  ๋ชฉ์ ์ ์ํด ์ธ์๋ก ๋๊ฒจ์ง๋ ํจ์



>   7.   **.forEach((element[, index[, array]]) => { element * 2 })**
>        *   ๋ฉ์๋๊ฐ ์ ์ฉ๋ ๋ฐฐ์ด์ ๊ฐ ์์๊ฐ ์ฝ๋ฐฑ ํจ์์ ์ํด ๊ฐฑ์ ๋จ ์ฆ, **๋ฐํ๊ฐ์ด ์์**
>        *   break, continue keyword ์ฌ์ฉ ๋ถ๊ฐ
>   8.   **.map((element[, index[, array]]) => { element * 2 })**
>        *   ๊ฐ ์์์ ๋ํ ์ฝ๋ฐฑ ํจ์์ ๋ฐํ๊ฐ์ ์์๋ก ๊ฐ๋ ์๋ก์ด ๋ฐฐ์ด ๋ฐํ
>   9.   **.filter((element[, index[, array]]) => { element % 2 })**
>        *   ๊ฐ ์์์ ๋ํ ์ฝ๋ฐฑ ํจ์์ ๊ฒฐ๊ณผ๊ฐ true์ธ ์์๋ง์ ๊ฐ๋ ์๋ก์ด ๋ฐฐ์ด ๋ฐํ
>   10.   **.reduce((acc, element[, index[, array]]) => { acc + element }, initial_value)**
>         *   ๊ฐ ์์์ ๋ํ ์ฝ๋ฐฑ ํจ์์ ๊ฒฐ๊ณผ๋ฅผ acc์ ๋์ ํ ํ, ์ต์ข ๋์ ๊ฐ์ ๋ฐํ
>         *   initial_value๋ฅผ ์ค์ ํ๋ฉด, ์ฝ๋ฐฑ ํจ์๊ฐ ์ต์ด๋ก ํธ์ถ๋  ๋ acc์ ํด๋น ๊ฐ์ด ํ ๋น๋๋ฉฐ, ๊ธฐ๋ณธ๊ฐ์ ๋ฐฐ์ด์ ์ฒซ๋ฒ์งธ ์์
>             *   ๋น ๋ฐฐ์ด์ ๋ํด ๋ฉ์๋๋ฅผ ์ ์ฉํ  ๋, initial_value๊ฐ ์ค์ ๋์ด ์์ง ์์ผ๋ฉด ์๋ฌ ๋ฐ์
>   11.   **.find((element[, index[, array]]) => { element % 2  === 1 })**
>         *   ์ฝ๋ฐฑ ํจ์์ ๋ฐํ๊ฐ์ด true์ธ ์์๋ฅผ ๋ฐํ
>         *   ๋ง์ฝ, ๋ฐํ๊ฐ์ด true์ธ ์์๊ฐ ์๋ค๋ฉด ์ฆ, ์ฐพ๋ ๊ฐ์ด ๋ฐฐ์ด ๋ด์ ์กด์ฌํ์ง ์๋๋ค๋ฉด, undefined๋ฅผ ๋ฐํ
>   12.   **.some((element[, index[, array]]) => { element % 2 })**
>         *   ๊ฐ ์์์ ๋ํ ์ฝ๋ฐฑ ํจ์์ ๋ฐํ๊ฐ ์ค ํ๋๋ผ๋ true์ด๋ฉด, true๋ฅผ ๋ฐํ
>         *   ๋ชจ๋  ์์์ ์ฝ๋ฐฑ ํจ์ ๋ฐํ๊ฐ์ด false์ด๋ฉด, false ๋ฐํ
>             *   ๋น ๋ฐฐ์ด์ ๋ํด์๋ ํญ์ false ๋ฐํ
>   13.   **.every((element[, index[, array]]) => { element % 2 })**
>         *   ๋ชจ๋  ์์์ ์ฝ๋ฐฑ ํจ์ ๋ฐํ๊ฐ์ด true์ด๋ฉด, true ๋ฐํ
>             *   ๋น ๋ฐฐ์ด์ ๋ํด์๋ ํญ์ true ๋ฐํ
>         *   ํ ์์๋ผ๋ ์ฝ๋ฐฑ ํจ์ ๋ฐํ๊ฐ์ด false์ด๋ฉด, false ๋ฐํ



#### B. Object Manipulation

>   1.   ์์ฑ๋ช ์ถ์ฝ
>
>        *   ```javascript
>            // ํ ๋นํ๋ ค๋ ๋ณ์๋ช๊ณผ ํค๊ฐ ๋์ผํ ๊ฒฝ์ฐ
>                    
>            const books = ['A', 'B']
>            const magazines = ['C', 'D']
>                    
>            const object = {
>                books,
>                magazines,
>            }
>            ```
>
>   2.   ๋ฉ์๋๋ช ์ถ์ฝ
>
>        *   ```javascript
>            // ๋ฉ์๋ ์ ์ธ ์, function keyword ์๋ต ๊ฐ๋ฅ
>                    
>            const object = {
>                method_name() {
>                    console.log('Hello, JavaScript! :)')
>                },
>            }
>            ```
>
>   3.   computed property name
>
>        *   ```javascript
>            // key๋ฅผ ํํ์์ ํ์ฉํ์ฌ ๋์ ์ผ๋ก ์์ฑ ๊ฐ๋ฅ
>                    
>            const key = 'KEY'
>            const val = ['A', 'B']
>                    
>            const object = {
>                [key]: value,
>            }
>            ```
>
>   4.   destructing assignment
>
>        *   ```javascript
>            // ๋ฐฐ์ด ํน์ ๊ฐ์ฒด๋ฅผ ๋ถํดํ์ฌ ๊ฐ ์์ฑ์ ๋ณ์์ ์ฝ๊ฒ ํ ๋นํ  ์ ์์
>                              
>            const object = {
>                name: 'name',
>                age: 'age',
>                phoneNumber: '010-1234-5678'
>            }
>                              
>            const { name, age, phoneNumber } = object
>            ```



#### C. JSON(JavaScript Object Notation)

>   JavaScript์ object์ ์ ์ฌํ์ง๋ง, ์ค์ ๋ก๋ ๊ทธ์  string ๋ฐ์ดํฐ ํ์์ด๋ฏ๋ก JavaScript์ object๋ก ์ฌ์ฉํ๊ธฐ ์ํด์๋ parsing ํ์



>   1.   **JSON.parse(json)**
>        *   JSON์ JavaScript์ object๋ก parsing
>   2.   **JSON.stringify(object)**
>        *   JavaScript์ object๋ฅผ JSON์ผ๋ก ๋ณํ

