# Applying 3D Convolutional Neural Networks to Identify Lung Nodules on Chest CT Scans

## Background
Lung Cancer is a heterogenous and aggressive form of cancer and is the leading cause of cancer death in men and women, accounting for etiology of 1 in every 4 cancer deaths in the United States. There were 224,000 new cases of lung cancer in 158,000 deaths caused by lung cancer in 2016.

The lifetime likelihood that a man will develop lung cancer in his lifetime is 1 in 14, whereas the risk for a woman is 1 in 17 in her lifetime.

The primary method in use by physicians to screen for lung cancer is  radiographic imaging of the Chest using Computed Tomography (CT) scans. This imaging modality makes use of many X-ray images to create a 3-dimensional representation of a patient's chest cavity. Unfortunately, Chest CT scans expose patients to a high level of radiation, on the order of 100-500 times the amount of radiation from a single x-ray.

Given the high prevalence of lung cancer screening and the harmful effects of excessive repeat radiation exposure, computational machine learning techniques have the potential to aid radiologists in their ability to spot lung nodules/tumors and minimize radiation exposure to patients. As Chest CT scans are representations of three-dimensional objects, I use a three-dimensional convolutional neural network to classify whether an area of the lung is likely to be healthy or a lung nodule/tumor.

## Neural Network Approach
*insert final study design*  

*insert image of final Neural Network architecture*


## Data
Data was collected from the Cancer Imaging Archive   http://www.cancerimagingarchive.net  

#### Datasets
**SPIE-AAPM Lung CT Challenge**    
*70 patients*  
https://wiki.cancerimagingarchive.net/display/DOI/SPIE-AAPM-NCI+Lung+Nodule+Classification+Challenge+Dataset  

**Lung Image Database Consortium Image Collection [LIDC-IDRI]**    
*1010 patients*  
https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI  


## Technologies Used

#### Amazon Web Services
EC2: G2 GPU instance  
  -1 GPU, 8 vCPU, 15 GiB Memory, 60GB SSD Storage  

#### Python Libraries  
Numpy  
Pandas  
scikit-learn  
PyDicom  
MoviePy  
Flask/HTML/CSS  

#### Neural Network Libraries  
Theano  
Lasagne  
CUDA/cuDNN [Nvidia]
