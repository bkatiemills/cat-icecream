FROM continuumio/miniconda:latest

# set up conda and apt-get
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda

# dependencies!
RUN conda install --yes python=2.7 nose matplotlib numpy pandas