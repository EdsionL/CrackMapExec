class CMEModule:
    '''
        Example
        Module by @yomama

    '''

    name = 'example module'

    description = 'Something Something'

    #If the module supports chaining, change this to True
    chain_support = False

    def options(self, context, module_options):
        '''Required. Module options get parsed here. Additionally, put the modules usage here as well'''
        pass

    def launcher(self, context, command):
        '''Required. Generate your launcher here'''
        pass

    def payload(self, context, command):
        '''Required. Generate your payload here'''
        pass

    def on_login(self, context, connection):
        '''Concurrent. Required if on_admin_login is not present. This gets called on each authenticated connection'''
        pass

    def on_admin_login(self, context, connection, launcher, payload):
        '''Concurrent. Required if on_login is not present. This gets called on each authenticated connection with Administrative privileges'''
        pass

    def on_request(self, context, request, launcher, payload):
        '''Optional. If the payload needs to retrieve additonal files, add this function to the module'''
        pass

    def on_response(self, context, response):
        '''Optional. If the payload sends back its output to our server, add this function to the module to handle its output'''
        pass