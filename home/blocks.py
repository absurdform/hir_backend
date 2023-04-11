from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class CardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(form_classname="title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")
    
    class Meta:
        icon = 'form'
