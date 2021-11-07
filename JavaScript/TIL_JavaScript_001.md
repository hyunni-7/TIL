# 🔥 TIL: JavaScript

>   *   **updated on:** 2021-11-07  23:03
>   *   **written by:** Sanghyun Park



#### 📌 References

>   1.   **[Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)**
>   2.   **[typeof null](https://2ality.com/2013/10/typeof-null.html)**
>   2.   **[methods of Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#instance_methods)**



#### 📚 Contents

>   1.   ECMAScript6
>        1.   변수와 식별자
>        2.   타입과 연산자
>        3.   조건문과 반복문
>        3.   함수
>        3.   배열과 객체



<br>

## 1. ECMAScript 6

>   ECMA에서 ECMA-262 규격에 따라 정의한, 표준화된 JavaScript



##### 👉 Note

>   JavaScript는 ASI(Automatic Semicolon Insertion)에 의해 semicolon이 자동으로 삽입됨(선택적 사용 가능)



### 1.1. 변수와 식별자



#### A. 식별자 규칙

>   1.   문자, dollar, underscore로 시작
>   2.   대소문자 구분
>        1.   **camelCase**(lower-camel-case): 변수, 함수, 객체
>        2.   **PascalCase**(upper-camel-case): 클래스(생성자)
>        3.   **SNAKE_CASE**: 상수
>   3.   예약어 사용 불가



#### B. 변수 선언 키워드

>   1.   **let:** 재선언 불가능, 재할당 가능, 블록 스코프
>   2.   **const:** 재선언 불가능, 재할당 불가능, 블록 스코프
>   3.   **var:** 재선언 가능, 재할당 가능, 함수 스코프, hoisting 발생
>        *   **hoisting:** 변수가 선언된 위치보다 앞에서 해당 변수가 참조되는 현상(undefined 반환)



##### 👉 Note

>   *   **블록 스코프**는 if문, for문, 함수 등의 중괄호({}) 내부를 지칭하는 개념으로 특정 블록 내 변수는 해당 블록의 외부에서 접근할 수 없음
>   *   **함수 스코프**는 함수의 중괄호({}) 내부를 지칭하는 개념으로 특정 함수 내 변수는 함수 바깥에서 접근할 수 없음



<br>

### 1.2. 데이터 타입과 연산자



#### A. 데이터 타입

>   1.   **Primitive Type:** 변수에 해당 타입의 실제 값이 저장됨, 다른 변수로 복사할 때 해당 값이 복사됨
>
>        1.   **Number**
>
>             *   NaN(Not-a-Number): 계산 불가능한 경우에 반환되는 값
>
>        2.   **String**
>
>             *   Template Literal: backtick으로 감싸진 문자열에 `${expression}`을 활용하여 표현식을 삽입할 수 있음
>
>        3.   **Boolean**
>
>             *   ToBoolean Conversion
>                 *   true: Object
>                 *   false: Undefined, Null, Number(0, -0, NaN), String(빈 문자열)
>
>        4.   **Undefined**
>
>        5.   **Null**
>
>             *   In JavaScript, `typeof null` is `'object'`, which incorrectly suggests that `null` is an object (it isn’t, it’s a primitive value, consult my blog post on [categorizing values](http://2ality.com/2013/01/categorizing-values.html) for details). This is a bug and one that unfortunately can’t be fixed, because it would break existing code.
>
>             
>
>   2.   **Reference Type:** 변수에 해당 객체의 참조 값이 저장됨, 다른 변수로 복사할 때 해당 객체의 참조 값이 복사됨



##### 👉 Note

>   **typeof:** 해당 변수의 데이터 타입을 확인하기 위한 연산자



##### 👉 Note

>   *   숫자형 데이터와 문자열 데이터에 대해 더하기(Number + String) 연산을 수행하면 숫자형 데이터가 문자열 데이터로 형변환된 후 concatenation이 수행됨
>   *   숫자형 데이터와 불리언 데이터에 대해 더하기(Number + Boolean) 연산을 수행하면 불리언 데이터가 숫자형 데이터로 형변환된 후 산술연산이 수행됨



#### B. 연산자

>   1.   **할당 연산자(`=`)**
>        1.   Increment 연산자(`variable++)`: 피연산자의 값을 1 증가시킴
>        2.   Decrement 연산자(`variable--)`: 피연산자의 값을 1 감소시킴
>   2.   **비교 연산자**
>        *   알파벳 비교는 사전 순서상 후 순위일수록 큰 값으로 평가되며, 소문자가 대문자보다 더 크다고 판정됨
>   3.   **동등 비교 연산자(`==`)**
>        *   암묵적 타입 변환을 수행하여 비교 대상들의 타입을 일치시킨 후 서로 같은 값인지 평가
>   4.   **일치 비교 연산자(`===`)**
>        *   엄격한 비교 즉, 비교 대상들의 데이터 타입과 값을 모두 비교하여 서로 같은 값인지 평가
>   5.   **논리 연산자(단축 평가 지원)**
>        *   and: &&
>        *   or: ||
>        *   not: !
>   6.   **Ternary Operator**(`expression ? value_when_true : value_when_false`)



<br>

### 1.3. 조건문과 반복문



#### A. 조건문

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
>                    break  // break가 없는 경우, 다음 case로 fall-through가 됨
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



#### B. 반복문

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
>                    console.log(attribute)  // object의 attribute(key: value)를 순회하며 출력하면 key가 출력됨
>                }
>                ```
>        
>        3.  **for of**
>        
>            *   순회 가능한 객체에 사용 가능
>        
>                *   string, array, set, map
>                *   object는 순회 가능한 객체가 아님(Uncaught TypeError 발생)
>        
>            *   ```javascript
>                for (element of iterables) {
>                    console.log(element)
>                }
>                ```



<br>

### 1.4. 함수



##### 👉 Note

>   *   JavaScript의 함수는 First-class object에 해당하므로, (1) 변수에 할당 가능하고, (2) 매개변수로 전달될 수 있으며, 또한 (3) 반환값으로 전달 받을 수 있음



#### A. function statement

>   1.   **Function Declaration**
>
>        *   hoisting이 발생할 수 있음
>
>        *   ```javascript
>            function func_name(args) {
>                console.log(args)
>            }
>            ```
>
>   2.   **Function Expression**
>
>        *   hoisting이 발생하지 않음
>            *   var keyword로 function expression을 작성한 경우, 해당 변수는 선언 전에 undefined로 초기화되어 Uncaught TypeError 발생
>
>        *   ```javascript
>            const variable = function (arg = default_value) {  // default argument
>                console.log(args)
>            }
>            ```



#### B. Arrow Function

>   1.   축약 과정
>
>        *   ```javascript
>            // step 0. function expression
>            const variable = function (args) {
>                return args * 2
>            }
>                              
>            // step 1. function keyword 생략
>            const variable = (args) => {
>                return args * 2
>            }
>                              
>            // step 2. 매개 변수의 개수가 한 개일 때, 소괄호 생략
>            const variable = args => {
>                return args * 2
>            }
>                              
>            // step 3. 함수 body의 표현식이 한 개일 때, return keyword와 중괄호 생략
>            const variable = args => args * 2
>            ```



<br>

### 1.5. 배열과 객체

>   **배열**
>
>   *   원소의 순서가 보장됨
>   *   0과 양의 정수로 인덱싱 가능
>   *   음의 정수로는 인덱싱 불가(undefined 반환)



>   **객체**
>
>   *   key는 문자열 타입만 가능
>       *   key가 한 단어로 구성된 경우 따옴표를 사용하지 않아도 됨
>   *   value는 모든 타입이 가능
>   *   객체의 속성(property)은 dot(`.`) 혹은 대괄호로 접근 가능
>       *   key에 구분자가 속해 있으면, 해당 key의 value는 대괄로로 접근해야 함



#### A. Array Methods

>   1.   **.reverse()**
>   2.   **.push(element) & .pop()**
>   3.   **.unshift(element) & .shift()**
>   4.   **.includes()**
>   5.   **.indexOf()**
>        *   해당 배열에 찾고자 하는 원소가 여러 개 존재하는 경우, 가장 앞선 인덱스 반환
>        *   해당 배열에 찾고자 하는 원소가 존재하지 않는 경우, **-1** 반환
>   6.   **.join(separator=',')**



##### 👉 Note

>   *   callback function
>       *   어떤 함수 내부에서 실행될 목적에 의해 인자로 넘겨지는 함수



>   7.   **.forEach((element[, index[, array]]) => { element * 2 })**
>        *   메소드가 적용된 배열의 각 원소가 콜백 함수에 의해 갱신됨 즉, **반환값이 없음**
>        *   break, continue keyword 사용 불가
>   8.   **.map((element[, index[, array]]) => { element * 2 })**
>        *   각 원소에 대한 콜백 함수의 반환값을 원소로 갖는 새로운 배열 반환
>   9.   **.filter((element[, index[, array]]) => { element % 2 })**
>        *   각 원소에 대한 콜백 함수의 결과가 true인 원소만을 갖는 새로운 배열 반환
>   10.   **.reduce((acc, element[, index[, array]]) => { acc + element }, initial_value)**
>         *   각 원소에 대한 콜백 함수의 결과를 acc에 누적한 후, 최종 누적값을 반환
>         *   initial_value를 설정하면, 콜백 함수가 최초로 호출될 때 acc에 해당 값이 할당되며, 기본값은 배열의 첫번째 원소
>             *   빈 배열에 대해 메소드를 적용할 때, initial_value가 설정되어 있지 않으면 에러 발생
>   11.   **.find((element[, index[, array]]) => { element % 2  === 1 })**
>         *   콜백 함수의 반환값이 true인 원소를 반환
>         *   만약, 반환값이 true인 원소가 없다면 즉, 찾는 값이 배열 내에 존재하지 않는다면, undefined를 반환
>   12.   **.some((element[, index[, array]]) => { element % 2 })**
>         *   각 원소에 대한 콜백 함수의 반환값 중 하나라도 true이면, true를 반환
>         *   모든 원소의 콜백 함수 반환값이 false이면, false 반환
>             *   빈 배열에 대해서는 항상 false 반환
>   13.   **.every((element[, index[, array]]) => { element % 2 })**
>         *   모든 원소의 콜백 함수 반환값이 true이면, true 반환
>             *   빈 배열에 대해서는 항상 true 반환
>         *   한 원소라도 콜백 함수 반환값이 false이면, false 반환



#### B. Object Manipulation

>   1.   속성명 축약
>
>        *   ```javascript
>            // 할당하려는 변수명과 키가 동일한 경우
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
>   2.   메서드명 축약
>
>        *   ```javascript
>            // 메소드 선언 시, function keyword 생략 가능
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
>            // key를 표현식을 활용하여 동적으로 생성 가능
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
>            // 배열 혹은 객체를 분해하여 각 속성을 변수에 쉽게 할당할 수 있음
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

>   JavaScript의 object와 유사하지만, 실제로는 그저 string 데이터 타입이므로 JavaScript의 object로 사용하기 위해서는 parsing 필요



>   1.   **JSON.parse(json)**
>        *   JSON을 JavaScript의 object로 parsing
>   2.   **JSON.stringify(object)**
>        *   JavaScript의 object를 JSON으로 변환

