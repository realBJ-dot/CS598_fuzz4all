// Function to simulate fetching user data
function fetchUserData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([
        { id: 1, name: 'John Doe', age: 30 },
        { id: 2, name: 'Jane Doe', age: 25 }
      ]);
    }, 1000);
  });
}

// Function to process user data
function processUserData(users) {
  return users.map(user => {
    const greeting = `Hello, ${user.name}!`;
    return { ...user, greeting };
  });
}

// Main function to fetch and process user data
function main() {
  fetchUserData().then(users => {
    const processedUsers = processUserData(users);
    console.log('Processed Users:', processedUsers);
  }).catch(error => {
    console.error('An error occurred:', error);
  });
}

// Run the main function
main();
