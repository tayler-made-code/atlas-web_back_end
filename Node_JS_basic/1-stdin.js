// Prompts user to input their name
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// reads user input and displays it if not null
process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    process.stdout.write('Your name is: ');
    process.stdout.write(chunk);
  }
});

// Closes the program and displays a cheeky message
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
