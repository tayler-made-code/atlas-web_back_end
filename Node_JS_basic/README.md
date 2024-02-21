# Resources

### Read or watch:

- [Node.js Ultimate Beginner’s Guide in 7 Easy Steps](https://www.youtube.com/watch?v=ENrzD9HAZK4)

- [Node JS getting started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)

- [Process API doc](https://node.readthedocs.io/en/latest/api/process/)

- [Child process](https://nodejs.org/api/child_process.htm)

- [Express getting started](https://expressjs.com/en/starter/installing.html)

- [Mocha documentation](https://mochajs.org/)

- [Nodemon documentation](https://github.com/remy/nodemon#nodemon)


# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- run javascript using NodeJS
- use NodeJS modules
- use specific Node JS module to read files
- use `process` to access command line arguments and the environment
- create a small HTTP server using Node JS
- create a small HTTP server using Express JS
- create advanced routes with Express JS
- use ES6 with Node JS with Babel-node
- use Nodemon to develop faster


# Requirements

- Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `node` (version 12.x.x)
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `js` extension
- Your code will be tested using `Jest` and the command npm run test
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`
- All of your functions/classes must be exported by using this format: `module.exports = myFunction;`


# Provided files

## <b>database.csv</b>
```sh
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
```

## <b>package.json</b>
<details>
  <summary>Click to show/hide file contents</summary>

  ```js
  {
    "name": "node_js_basics",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
      "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1"
    },
    "devDependencies": {
      "babel-cli": "^6.26.0",
      "babel-preset-env": "^1.7.0",
      "nodemon": "^2.0.2",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
  ```
</details>

## <b>babel.config.js</b>
<details>
  <summary>Click to show/hide file contents</summary>

  ```js
  module.exports = {
    presets: [
      [
        '@babel/preset-env',
        {
          targets: {
            node: 'current',
          },
        },
      ],
    ],
  };
  ```
</details>

## <b>.eslintrc.js</b>
<details>
  <summary>Click to show/hide file contents</summary>

  ```js
  module.exports = {
    env: {
      browser: false,
      es6: true,
      jest: true,
    },
    extends: [
      'airbnb-base',
      'plugin:jest/all',
    ],
    globals: {
      Atomics: 'readonly',
      SharedArrayBuffer: 'readonly',
    },
    parserOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
    },
    plugins: ['jest'],
    rules: {
      'max-classes-per-file': 'off',
      'no-underscore-dangle': 'off',
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
    overrides:[
      {
        files: ['*.js'],
        excludedFiles: 'babel.config.js',
      }
    ]
  };
  ```
</details>

and…
## Don’t forget to run `$ npm install` when you have the `package.json`

### To run linter use ./node_modules/.bin/eslint "filename.js"

---

# Tasks

---

## 0. Executing basic javascript with Node JS

In the file `0-console.js`, create a function named `displayMessage` that prints in `STDOUT` the string argument

```
Obi-Wan@Kenobi-MBP$ cat 0-main.js
const displayMessage = require('./0-console');

displayMessage("Hello NodeJS!");

Obi-Wan@Kenobi-MBP$ node 0-main.js
Hello NodeJS!
Obi-Wan@Kenobi-MBP$
```

---

## 1. Using Process stdin

Create a program named `1-stdin.js` that will be executed through command line:
  - It should display the message `Welcome to Holberton School, what is your name?` (followed by a new line)
  - The user should be able to input their name on a new line
  - The program should display `Your name is: INPUT`
  - When the user ends the program, it should display `This important software is now closing` (followed by a new line)

  <b>Requirements:</b>
  - Your code will be tested through a child process, make sure you have everything you need for that.

```
Obi-Wan@Kenobi-MBP$ node 1-stdin.js 
Welcome to Holberton School, what is your name?
Bob
Your name is: Bob
Obi-Wan@Kenobi-MBP$ 
Obi-Wan@Kenobi-MBP$ echo "John" | node 1-stdin.js 
Welcome to Holberton School, what is your name?
Your name is: John
This important software is now closing
Obi-Wan@Kenobi-MBP$
```

---

## 2. Reading a file synchronously with Node JS

Using the database `database.csv` (provided in project description), create a function `countStudents` in the file `2-read_file.js`

Create a function named `countStudents`. It should accept a path in argument
The script should attempt to read the database file synchronously
If the database is not available, it should throw an error with the text `Cannot load the database`
If the database is available, it should log the following message to the console `Number of students: NUMBER_OF_STUDENTS`
It should log the number of students in each field, and the list with the following format: `Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES`
CSV file can contain empty lines (at the end) - and they are not a valid student!

```
Obi-Wan@Kenobi-MBP$ cat 2-main_0.js
const countStudents = require('./2-read_file');

countStudents("nope.csv");

Obi-Wan@Kenobi-MBP$ node 2-main_0.js
2-read_file.js:9
    throw new Error('Cannot load the database');
    ^

Error: Cannot load the database
...
Obi-Wan@Kenobi-MBP$
Obi-Wan@Kenobi-MBP$ cat 2-main_1.js
const countStudents = require('./2-read_file');

countStudents("database.csv");

Obi-Wan@Kenobi-MBP$ node 2-main_1.js
Number of students: 10
Number of students in CS: 6. List: Johann, Arielle, Jonathan, Emmanuel, Guillaume, Katie
Number of students in SWE: 4. List: Guillaume, Joseph, Paul, Tommy
Obi-Wan@Kenobi-MBP$ 
```