from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from fiscales.models import Fiscales, Historial
from fiscales.forms import Formularios
# from fiscales.forms import Formularios
from django.db.models import Q 


def listaFiscales(request):
    fiscales = Fiscales.objects.all()
    return render(request, 'listaFiscales.html', {"fiscales":fiscales})



def buscar_fiscal(request):
        queryset = request.GET.get("buscar")
        if queryset:

            fiscales = Fiscales.objects.filter(
                Q(nombre_sucursal__icontains = queryset) |
                Q(numero_serie__icontains= queryset) |
                Q(punto_venta__icontains = queryset) |
                Q(modelo_fiscal__icontains = queryset)
            ).distinct()

            if not fiscales:
                return render(request, 'listaFiscales.html', {"busqueda":queryset, "msg":'No data'})

            return render(request, 'listaFiscales.html', {"fiscales":fiscales})
        else:
            return render(request, 'listaFiscales.html', {"busqueda":queryset, "msg":'No data'})
        

def registrarFiscal(request):
        fiscal = Formularios()
        return render(request, 'agregarFiscal.html', {"form":fiscal})

def guardarFiscal(request):
        #if request.method == 'POST'
        fiscal = Formularios(request.POST)

        if fiscal.is_valid(): #validar que la informacion del request es true
            fiscal.save() #guardar en la db
            fiscal = Formularios() #instanciar de nuevo para limpiar lo campos

        return render(request, 'agregarFiscal.html', {"form":fiscal, "msg":"agregado"}) 
