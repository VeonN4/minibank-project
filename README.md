# About this project

This project was created as the final semester assignment for Pak Yayat's class, and it serves as a learning platform to explore database concepts. The project is a mini-bank application developed using Python and MongoDB.

# Getting Started

Before you can run the script, there's a few steps to get started. Please follow the instructions below!

## Requirements
- MongoDB 
- Python
- Docker (Optional)

### 1. Set up virtual environment

First, you need to create a virtual environment. Why is this important? Because they allow you to create isolated spaces for different projects, preventing conflicts between dependencies. 
You can simply type the following command to create the virtual 

```
python -m venv [name of virtual environment].
```

### 2. Installation Requirements

After you have created the virtual environment, you need to install the library required by the script. To install it, you can use the following command.

```
pip install -r requirements.txt
```
alternatively
```
python -m pip install -r requirements.txt
```

### 3. Setting up environment variables

Before you can really run it. You need to modify the .env file first. to do that, just follow the instructions below
1. Rename `.env.example` to `.env`.
2. Open the file and change the `MONGODB_ADDRESS` to your own MongoDB database.

>[!NOTE]
>The `MONGODB_USER` and `MONGODB_PASSWORD` are for **Docker Compose**. If you don't use them, just ignore them.

### 4. Running the script

Now you can just run the script, you can use the following command to run the script.

```
python main.py
```

# Self-hosting MongoDB

If you want to run your own MongoDB, I have already provided a Docker Compose file for you. For more information on how to use it, you can do your own research (I'm too lazy to create the documentation). 
