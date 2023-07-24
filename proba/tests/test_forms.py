from django.test import TestCase
from jobs.models import Tag, Job
from jobs.forms import JobForm, TagForm


class TagFormTestInputValid(TestCase):
    def test_tag_form_valid_input(self):
        form = TagForm(data={'name': 'Contrary'})
        self.assertTrue(form.is_valid())

    def test_tag_form_no_input(self):
        form = TagForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_tag_form_invalid_input(self):
        form = TagForm(data={'name': 'Contrary to popular belief, Lorem Ipsum is not simply random text. \
                                    It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \
                                    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, \
                                    looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, \
                                    from a line in section 1.10.32. ', })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class JobFormTestFieldLabels(TestCase):
    def test_job_form_test_field_labels(self):
        form = JobForm()

        self.assertTrue(form.fields['title'].label == 'Title')
        self.assertTrue(form.fields['logo'].label == 'Please add your logo')
        self.assertTrue(form.fields['tags'].label ==
                        'Tags - please select standard tags')
        self.assertTrue(form.fields['custom_tags'].label ==
                        'Custom tags - please separate tags with a comma')
        self.assertTrue(form.fields['company'].label == 'Company')
        self.assertTrue(form.fields['location'].label == 'Location')
        self.assertTrue(form.fields['email'].label == 'Email')
        self.assertTrue(form.fields['website'].label == 'Website')
        self.assertTrue(form.fields['description'].label == 'Description')


class JobFormTestInputValid(TestCase):
    def test_job_form_valid_input(self):
        test_tag1 = Tag.objects.create(name='Test Tag 1')
        test_tag2 = Tag.objects.create(name='Test Tag 2')
        test_tag3 = Tag.objects.create(name='Test Tag 3')
        form = JobForm(data={
            'title': 'Contrary to popular belief',
            'tags': [test_tag1.pk, test_tag2.pk, test_tag3.pk],
            'custom_tags': 'ddd, qqqq, wwww, eeee, test',
            'company': 'Contrary to popular belief',
            'location': 'Contrary to popular belief',
            'email': 'testemail@test.com',
            'website': 'www.test.com',
            'description': 'Contrary to popular belief, Lorem Ipsum is not simply random text.'
        })

        self.assertTrue(form.is_valid())

    def test_job_form_no_input(self):
        form = JobForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 8)


class JobFormTestInputInvalid(TestCase):
    def test_job_form_input_invalid(self):
        form = JobForm(data={
            'title': 'Contrary to popular belief, Lorem Ipsum is not simply random text. \
                                    It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \
                                    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, \
                                    looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, \
                                    and going through the cites of the word in classical literature, discovered the undoubtable source. \
                                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" \
                                    (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, \
                                    very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes \
                                    from a line in section 1.10.32. ',
            'tags': '',
            'custom_tags': 'Contrary to popular belief, Lorem Ipsum is not simply random text. \
                                    It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \
                                    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, \
                                    looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, \
                                    and going through the cites of the word in classical literature, discovered the undoubtable source. \
                                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" \
                                    (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, \
                                    very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes \
                                    from a line in section 1.10.32. \
                                    ',
            'company': 'Contrary to popular belief, Lorem Ipsum is not simply random text. \
                                    It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \
                                    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, \
                                    looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, \
                                    and going through the cites of the word in classical literature, discovered the undoubtable source. \
                                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" \
                                    (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, \
                                    very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes \
                                    from a line in section 1.10.32. \
                                    ',
            'location': 'Contrary to popular belief, Lorem Ipsum is not simply random text. \
                                    It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. \
                                    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, \
                                    looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, \
                                    and going through the cites of the word in classical literature, discovered the undoubtable source. \
                                    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" \
                                    (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, \
                                    very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes \
                                    from a line in section 1.10.32. \
                                    ',
            'email': 'Contrary to popular belief',
            'website': 'Contrary to popular belief',
            'description': 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                                    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. \
                               '

        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 8)
        self.assertEqual(len(form['title'].errors), 1)
        self.assertEqual(len(form['tags'].errors), 1)
        self.assertEqual(len(form['custom_tags'].errors), 1)
        self.assertEqual(len(form['company'].errors), 1)
        self.assertEqual(len(form['location'].errors), 1)
        self.assertEqual(len(form['email'].errors), 1)
        self.assertEqual(len(form['website'].errors), 1)
        self.assertEqual(len(form['description'].errors), 1)
