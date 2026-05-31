// client.js
const API_BASE_URL = 'http://127.0.0.1:8000';
const targetPostId = 1;

async function runApiDemo() {
    try {
        // =======================================================
        // STEP 1: Fetch the initial post and its comments
        // =======================================================
        console.log("--- STEP 1: Fetching Initial Post ---");
        
        let response = await fetch(`${API_BASE_URL}/posts/${targetPostId}`);
        let postData = await response.json();
        
        console.log("Initial Post Data from Server:", postData);
        console.log(`Current Comment Count: ${postData.comments.length}`);


        // =======================================================
        // STEP 2: Send a POST request to add a new comment
        // =======================================================
        console.log("\n--- STEP 2: Submitting a New Comment ---");
        
        let commentResponse = await fetch(`${API_BASE_URL}/posts/${targetPostId}/comments`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Tells the server we are sending JSON data
            },
            body: JSON.stringify({ 
                text: "Wow, seeing the actual code execution clears things up!" 
            })
        });
        
        let commentResult = await commentResponse.json();
        console.log("Server Response to POST:", commentResult);


        // =======================================================
        // STEP 3: Fetch the updated post to verify changes
        // =======================================================
        console.log("\n--- STEP 3: Fetching Updated Post ---");
        
        response = await fetch(`${API_BASE_URL}/posts/${targetPostId}`);
        postData = await response.json();
        
        console.log("Updated Post Data from Server:", postData);
        console.log(`New Comment Count: ${postData.comments.length}`);

    } catch (error) {
        console.error("An error occurred during API communication:", error);
    }
}

// Execute the workflow
runApiDemo();