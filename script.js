import { GoogleGenerativeAI } from '@google/generative-ai';
import * as readline from 'node:readline/promises';

const API_KEY = "AIzaSyCqc3zIUa59r7UvNbn7gy6rhRXbsZ6NcxE"; 

const genAI = new GoogleGenerativeAI(API_KEY);

async function runChat() {
    const model = genAI.getGenerativeModel({
        model: 'gemini-1.5-flash',
        generationConfig: {
            temperature: 0.25,
            top_p: 0.95,
            top_k: 40,
            max_output_tokens: 8192,
            response_mime_type: "text/plain",
        },
        safetySettings: [],
        systemInstruction: "your name is SafeBrowse you are an AI agent who is responsible for detecting and recognizing harmful content, including misinformation, hate speech, and cyberbullying, from given data, and should highlight such content, provide corrections, and suggest appropriate actions accordingly, also you are made by the team 404 fixers, if data has been given with the intension not related to your main mission you should just explain why its not from your expertise, also tell about yourself only when asked.",
    });

    let history = [];

    console.log("Bot: Hello, how can I help you?");

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    const promptUser = async () => {
        try {
            const userInput = await rl.question('You: ');

            const messages = history.map(turn => ({
                role: turn.role,
                parts: turn.parts.map(part => ({ text: part.text }))
            }));

            // Add user input
            messages.push({ role: "user", parts: [{ text: userInput }] });

            // Generate response
            const result = await model.generateContent({ contents: messages });

            const modelResponse = result.response.text(); // Extract response text

            console.log(`Bot: ${modelResponse}\n`);

            // Store conversation history
            history.push({ role: 'user', parts: [{ text: userInput }] });
            history.push({ role: 'model', parts: [{ text: modelResponse }] });

            promptUser();
        } catch (error) {
            console.error("Error during conversation:", error);
            rl.close();
        }
    };

    promptUser();
}

runChat();
