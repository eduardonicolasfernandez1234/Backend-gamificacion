from usuarios.models import Usuario
from juego.models import Pregunta, Logro, Estatus, Canjeo, ProductoCanjeo

def registrarPuntos(usuario: Usuario, pregunta: Pregunta, correcto: bool, ayuda: bool = False):
    if correcto:
        usuario.puntaje_total = usuario.puntaje_total + pregunta.puntos_correcto
        usuario.puntaje_diario = usuario.puntaje_diario + pregunta.puntos_correcto
        usuario.rachas_preguntas = usuario.rachas_preguntas + 1
    else:
        usuario.rachas_preguntas = 0
        if usuario.puntaje_total - pregunta.puntos_incorrecto < 1:
            usuario.puntaje_total = 0
            usuario.puntaje_diario = 0
        else:
            usuario.puntaje_total = usuario.puntaje_total - pregunta.puntos_incorrecto
            usuario.puntaje_diario = usuario.puntaje_diario - pregunta.puntos_incorrecto
    usuario.save()
    registrarAyuda(usuario, ayuda)
    logros = Logro.objects.all()
    revisarLogroPorCategoria(usuario, logros)
    lista_estatus = Estatus.objects.all()
    revisarEstatusActual(usuario, lista_estatus)


def registrarAyuda(usuario: Usuario, ayuda: bool):
    if ayuda:
        usuario.cantidad_ayuda_solicitada = usuario.cantidad_ayuda_solicitada + 1
        usuario.save()


def revisarLogroPorCategoria(usuario: Usuario, logros):
    for logro in logros:
        print(logro.categoria)
        if logro.categoria == 1:
            revisarCategoriaPuntosDiarios(usuario, logro)
        elif logro.categoria == 2:
            revisarCategoriaInicioConsecutivo(usuario, logro)
        elif logro.categoria == 3:
            revisarCategoriaRespuestaConsecutiva(usuario, logro)
        elif logro.categoria == 4:
            revisarCategoriaAyudaSolicitada(usuario, logro)

def revisarCategoriaPuntosDiarios(usuario: Usuario, logro: Logro):
    if logro.temporal:
        print('LOGRO TEMPORAL')
        if logro.nombre not in usuario.logros_temporal:
            print('El logro no esta en el listado de usuarios')
            if logro.puntos_diarios <= usuario.puntaje_diario:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros_temporal.append(logro.nombre)
                usuario.save()
            else:
                print('No alcanza los puntos todavia')
        else:
            print('El logro esta en el listado de usuarios')
    else:
        print('LOGRO NO TEMPORAL')
        if logro.nombre not in usuario.logros:
            print('El logro no esta en el listado de usuarios')
            if logro.puntos_diarios <= usuario.puntaje_total:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros.append(logro.nombre)
                usuario.save()
        

def revisarCategoriaInicioConsecutivo(usuario: Usuario, logro: Logro):
    if logro.temporal:
        print('LOGRO TEMPORAL')
        if logro.nombre not in usuario.logros_temporal:
            print('El logro no esta en el listado de usuarios')
            if logro.inicio_consecutivo == usuario.inicio_sesion_consecutivo:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros_temporal.append(logro.nombre)
                usuario.save()
            else:
                print('No alcanza los puntos todavia')
        else:
            print('El logro esta en el listado de usuarios')
    else:
        print('LOGRO NO TEMPORAL')
        if logro.nombre not in usuario.logros:
            print('El logro no esta en el listado de usuarios')
            if logro.inicio_consecutivo == usuario.inicio_sesion_consecutivo:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros.append(logro.nombre)
                usuario.save()

def revisarCategoriaRespuestaConsecutiva(usuario: Usuario, logro: Logro):
    if logro.temporal:
        print('LOGRO TEMPORAL')
        if logro.nombre not in usuario.logros_temporal:
            print('El logro no esta en el listado de usuarios')
            if logro.respuesta_consecutiva == usuario.rachas_preguntas:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros_temporal.append(logro.nombre)
                usuario.save()
            else:
                print('No alcanza los puntos todavia')
        else:
            print('El logro esta en el listado de usuarios')
    else:
        print('LOGRO NO TEMPORAL')
        if logro.nombre not in usuario.logros:
            print('El logro no esta en el listado de usuarios')
            if logro.respuesta_consecutiva == usuario.rachas_preguntas:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros.append(logro.nombre)
                usuario.save()

def revisarCategoriaAyudaSolicitada(usuario: Usuario, logro: Logro):
    if logro.temporal:
        print('LOGRO TEMPORAL')
        if logro.nombre not in usuario.logros_temporal:
            print('El logro no esta en el listado de usuarios')
            if logro.ayuda_solicitada == usuario.cantidad_ayuda_solicitada:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros_temporal.append(logro.nombre)
                usuario.save()
            else:
                print('No alcanza los puntos todavia')
        else:
            print('El logro esta en el listado de usuarios')
    else:
        print('LOGRO NO TEMPORAL')
        if logro.nombre not in usuario.logros:
            print('El logro no esta en el listado de usuarios')
            if logro.ayuda_solicitada == usuario.cantidad_ayuda_solicitada:
                print('Los puntos diarios del logro son menores, asigando nuevos puntos')
                usuario.puntaje_diario = usuario.puntaje_diario + logro.puntos_recompensa
                usuario.puntaje_total = usuario.puntaje_total + logro.puntos_recompensa
                usuario.logros.append(logro.nombre)
                usuario.save()

def revisarEstatusActual(usuario: Usuario, lista_estatus):
    for estatus in lista_estatus:
        # print(estatus.categoria)
        verificarEstatusUsuario(usuario, estatus)

def verificarEstatusUsuario(usuario: Usuario, estatus: Estatus):
    if usuario.estatus_actual:
        # print('HAY ESTATUS ACTUAL')
        if usuario.estatus_actual != estatus.nombre:
            #print('EL ESTATUS ES DIFERENTE AL ACTUAL')
            if estatus.puntos_base >= usuario.puntaje_total:
                # print('CUMPLE LOS PUNTOS')
                usuario.puntaje_total = usuario.puntaje_total + estatus.puntos_recompensa
                usuario.puntaje_diario = usuario.puntaje_diario + estatus.puntos_recompensa
                usuario.estatus_actual = estatus.nombre
    else:
        # print('NO HAY ESTATUS ACTUAL')
        if estatus.puntos_base >= usuario.puntaje_total:
            # print('CUMPLE LOS PUNTOS')
            usuario.puntaje_total = usuario.puntaje_total + estatus.puntos_recompensa
            usuario.puntaje_diario = usuario.puntaje_diario + estatus.puntos_recompensa
            usuario.estatus_actual = estatus.nombre


def canjearProducto(usuario: Usuario, producto: ProductoCanjeo):
    if usuario.puntaje_total >= producto.puntos_necesarios:
        usuario.puntaje_total = usuario.puntaje_total - producto.puntos_necesarios
        usuario.productos_canjeados.append(producto.pk)
        
