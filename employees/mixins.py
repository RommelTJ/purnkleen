class UserOwnerMixin(object):

    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form.add_error(None, "You are not allowed to edit this user.")
            return self.form_invalid(form)
