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


def generate_images(n: int):
    '''
    Generates a list of images and displayes
    Parameters:
        n (int): number of images to be generated
    Returns:
        (tensor): an array of generated images

    '''
    noise, _ = model.buildNoiseData(n)
    with torch.no_grad():
        generated_images: torch.tensor = model.test(noise)

    if n > 0:
        st.header('Сгенерированное изображение' if n ==
                  1 else 'Сгенерированные изображения')

    transform = T.ToPILImage()

    return [transform(tensor) for tensor in generated_images]


model = load_model()
# List of generated images, serves as a model in MVC pattern
imgs = []

##########
# Layout #
##########

st.title('FASHIONGEN')

number_of_images_field = st.number_input(
    'Количество изображений', value=0, min_value=0)

btn_col_1, btn_col_2 = st.columns(2)

with btn_col_1:
    if st.button('Run'):
        imgs = generate_images(number_of_images_field)

with btn_col_2:
    if st.button('Clear'):
        imgs = []


st.image(imgs)
