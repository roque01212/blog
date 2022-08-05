from django.db import models

class EntryManager(models.Manager):

    """ porcedimiento para entrada """

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,
        ).order_by('-created').first()#primer articulo
            # aunque no tenemos el atriburo creates el 
            #TimeStampedModel ya lo crea por defecto   

    def  entradas_en_home(self):
        # devuelve las ultias 4 entradas en home
        return self.filter(
            public=True,
            in_home=True,
        ).order_by('-created')[:4]


    def  entradas_recientes(self):
        # devuelve las ultias 6 entradas recientes
        return self.filter(
            public=True,
        ).order_by('-created')[:6]

    def buscar_entrada(self, kword, categoria):
        # procedimiento para buscar entradas por categoria o palabra clave
        if len(categoria)> 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
