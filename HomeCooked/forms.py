# This is our forms section




class MealForm(forms.ModelForm):
    class Meta:
      model = Meal
      fields = [
        'name',
        'description',
        'image_url',] 
# price is a different model. How do I link Can you add two models to one form