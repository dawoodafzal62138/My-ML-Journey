# 🐉 AI-Powered Text Adventure Engine

A modern, responsive, and highly customizable text-based adventure game engine built with Python. It uses **CustomTkinter** for a sleek graphical interface and integrates with **Google's Gemini API** (`gemini-3.1-flash-lite`) to act as a dynamic, intelligent Dungeon Master.

## ✨ Features

* **Dynamic AI Dungeon Master:** Powered by Gemini, the game remembers your inventory, tracks your health, and dynamically responds to any creative action you type.
* **Modern GUI:** Built with `customtkinter` for a dark-mode, sleek aesthetic.
* **Responsive Design:** Utilizes Python `threading` to ensure the UI never freezes while waiting for the AI to generate the next part of the story.
* **Immersive Chat UI:** Color-coded text tagging (Green for the player, Red for the AI, Blue for system messages) makes reading the story easy.
* **Graceful Error Handling:** Built-in rate limit detection catches 429 errors and warns the player instead of crashing the game.
* **Secure Key Entry:** Prompts the user for their API key via a secure dialog box upon launch, ensuring no sensitive keys are hardcoded into the script.

## 🚀 How to Run

Follow these steps to set up and play the game on your local machine.

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your computer. You will also need to get a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).

