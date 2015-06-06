from django import forms


class ClockSearchForm(forms.Form):
    """
    This is just ugly.
    Ugly. Bad Django!
    """
    
    DAYS = (('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            ('13', '13'),
            ('14', '14'),
            ('15', '15'),
            ('16', '16'),
            ('17', '17'),
            ('18', '18'),
            ('19', '19'),
            ('20', '20'),
            ('21', '21'),
            ('22', '22'),
            ('23', '23'),
            ('24', '24'),
            ('25', '25'),
            ('26', '26'),
            ('27', '27'),
            ('28', '28'),
            ('29', '29'),
            ('30', '30'),
            ('31', '31')
            )

    MONTHS = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),
            )
    
    #this made me thik of how many years this program will be operational.
    #15 years worth should be enough. Though ive seen code as
    #bad as this one last longer than that. The worse the code, the more it lasts.
    YEARS = (('2015', '2015'),
            ('2016', '2016'),
            ('2017', '2017'),
            ('2018', '2018'),
            ('2019', '2019'),
            ('2020', '2020'),
            ('2021', '2021'),
            ('2022', '2022'),
            ('2023', '2023'),
            ('2024', '2024'),
            ('2025', '2025'),
            ('2026', '2026'),
            ('2027', '2027'),
            ('2028', '2028'),
            ('2029', '2029'),
            ('2030', '2030'))


    #Rather than use the datetime select field 
    #it was decided, by the elders of the internet
    #that a regular select would do
    #because its simpler. Its ugly as fuck though!

    from_day = forms.ChoiceField(choices=DAYS, widget=forms.Select(attrs={'class':'form-control'}))
    from_month = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class':'form-control'}))
    from_year = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class':'form-control'}))
    
    to_day = forms.ChoiceField(choices=DAYS, widget=forms.Select(attrs={'class':'form-control'}))
    to_month = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class':'form-control'}))
    to_year = forms.ChoiceField(choices=YEARS, widget=forms.Select(attrs={'class':'form-control'}))