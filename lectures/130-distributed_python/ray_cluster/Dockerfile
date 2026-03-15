FROM rayproject/ray:latest-py310 

# Install the exact libraries needed for the lecture
RUN pip install --no-cache-dir \
    scikit-learn==1.7.2 \
    pandas==2.3.3 \
    numpy==2.2.6

# Set the working directory
WORKDIR /app


# --- DOCKER CHEAT SHEET FOR STUDENTS ---
# 1. BUILD: Build the image locally (run this if you change this file)
#    docker build -t ray-lecture-custom .
#
# 2. LIST: See all images stored on your laptop
#    docker images
#
# 3. CLEAN: Remove unused images to save disk space
#    docker image prune
#
# 4. INSPECT: See what's inside the image
#    docker run -it ray-lecture-custom /bin/bash