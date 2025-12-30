// Configuration - Change API_URL after deployment!
const API_URL = 'http://localhost:8000/api/chat';

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('chatbot-toggle');
    const close = document.getElementById('chatbot-close');
    const chatWindow = document.getElementById('chatbot-window');
    const input = document.getElementById('chatbot-input');
    const send = document.getElementById('chatbot-send');
    const messages = document.getElementById('chatbot-messages');

    let isOpen = false;

    // Toggle chatbot
    toggle.addEventListener('click', () => {
        isOpen = !isOpen;
        chatWindow.classList.toggle('hidden');

        if (isOpen) {
            input.focus();
            // Add welcome message if first time opening
            if (messages.querySelectorAll('.message').length <= 1) {
                // Welcome message is already in HTML
            }
        }
    });

    // Close chatbot
    close.addEventListener('click', () => {
        isOpen = false;
        chatWindow.classList.add('hidden');
    });

    // Send message on button click
    send.addEventListener('click', sendMessage);

    // Send message on Enter key
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    async function sendMessage() {
        const message = input.value.trim();
        if (!message) return;

        // Disable input while processing
        input.disabled = true;
        send.disabled = true;

        // Add user message
        addUserMessage(message);
        input.value = '';

        // Show typing indicator
        const typingIndicator = showTyping();

        try {
            // Call API
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            // Remove typing indicator
            typingIndicator.remove();

            // Add bot response
            if (data.success) {
                addBotMessage(data.response);
            } else {
                addBotMessage('Sorry, I couldn\'t process that. Please try again!');
            }

        } catch (error) {
            console.error('Error:', error);
            typingIndicator.remove();
            addBotMessage('Oops! Something went wrong. Please make sure the backend server is running on localhost:8000');
        } finally {
            // Re-enable input
            input.disabled = false;
            send.disabled = false;
            input.focus();
        }
    }

    function addUserMessage(text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message user';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = text;

        messageDiv.appendChild(contentDiv);
        messages.appendChild(messageDiv);
        scrollToBottom();
    }

    function addBotMessage(text) {
        const messageDiv = document.createElement('div');
        messageDiv.className = 'message bot';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = text;

        messageDiv.appendChild(contentDiv);
        messages.appendChild(messageDiv);
        scrollToBottom();
    }

    function showTyping() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot';

        const typingIndicator = document.createElement('div');
        typingIndicator.className = 'typing-indicator';
        typingIndicator.innerHTML = '<span></span><span></span><span></span>';

        typingDiv.appendChild(typingIndicator);
        messages.appendChild(typingDiv);
        scrollToBottom();
        return typingDiv;
    }

    function scrollToBottom() {
        messages.scrollTop = messages.scrollHeight;
    }

    // Close chatbot when clicking outside
    document.addEventListener('click', (e) => {
        if (isOpen && !chatWindow.contains(e.target) && !toggle.contains(e.target)) {
            isOpen = false;
            chatWindow.classList.add('hidden');
        }
    });

    // Keyboard shortcut to toggle chatbot (Ctrl + /)
    document.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === '/') {
            e.preventDefault();
            toggle.click();
        }
        // Escape to close
        if (e.key === 'Escape' && isOpen) {
            isOpen = false;
            chatWindow.classList.add('hidden');
        }
    });
});

console.log('Zeeshan AI Chatbot Widget - Loaded!');
