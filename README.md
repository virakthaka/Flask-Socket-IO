## Setup requirement 

1. Create a virtual environment

    for macOS/linux
    
        python3 -m venv env
           
    for window
            
        python -m venv env
                    
2. Activate/deactivate environment on project 
    
    Run command below to activate virtual environment
    
        source env/bin/activate
         
    Run command below to deactivate virtual environment
     
        deactivate
        
3. Install Flask in the virtual environment by running one of the following commands

    for macOS/Linux
    
        pip3 install flask
    
    for Windows
    
        pip install flask  
    

## Start Service

start app by follow the command below

    export FLASK_APP=run.py FLASK_ENV=development
    flask run --host=0.0.0.0


