import torch
import torchvision.transforms as T
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_model():
    use_gpu = True if torch.cuda.is_available() else False
    model = torch.hub.load('facebookresearch/pytorch_GAN_zoo:hub', 
                           'DCGAN', 
                           pretrained=True,
                           useGPU=use_gpu)
    return model

def text_field() -> str:
    return st.text_input('Количество изображений')

    
model = load_model()

st.title('FASHIONGEN')
text = text_field()
if st.button('Run') and len(text):
    try:
        num_of_images = int(text)
        if num_of_images <= 0:
            raise ValueError('Неверное значение поля')
    except ValueError:
        st.warning('Неверное значение')
    else: 
        noise, _ = model.buildNoiseData(num_of_images)
        with torch.no_grad():
            generated_images: torch.tensor = model.test(noise)
            
        st.title('Сгенерированное изображение')
        
        transform = T.ToPILImage()
        imgs = [transform(tensor) for tensor in generated_images]
        st.image(imgs)