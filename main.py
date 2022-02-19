import pygame
import os
import utls


def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        print("\n") * 120


def Menu():
    os.system("title Email Scraper")
    clear()
    print('----------------------------------')
    print('        Email Scraper')
    print('----------------------------------')
    print('[1] Input The List\n \n[2] Scrap from insert.txt\n \n[3] Exit Program\n')
    print('-----------------------------------------------------------------')
    print('                                                                 ')
    print('  Note: If You Are Using[2] Insert Your List Into "insert.txt"  ')
    print('                                                                 ')
    print('-----------------------------------------------------------------\n')
    option = str(input('Choose An Option: '))
    print("")
    if option == '1':
        clear()
        utls.mode('input')
        print('-----------------------------------------------------')
        print('      Process Completed Successfully!')
        print('\nThe Full List Has Been Saved In Leeched.txt')
        print('-----------------------------------------------------')
        pygame.time.wait(5000)
        print("")
        print("===> Returning Back To Menu")
        pygame.time.wait(1000)
        clear()
        Menu()
    elif option == '2':
        clear()
        utls.mode('txt')
        print('-----------------------------------------------------')
        print('      Process Completed Successfully!')
        print('\nThe Full List Has Been Saved In Leeched.txt')
        print('-----------------------------------------------------')
        pygame.time.wait(5000)
        print("")
        print("===> Returning Back To Menu")
        pygame.time.wait(1000)
        clear()
        Menu()
    elif option == '3':
        clear()
        print("")
        pygame.time.wait(250)
        print('Closing...')
        pygame.time.wait(250)
        print('Thank You For Using The Program!')
        pygame.time.wait(1000)
        exit()
    else:
        print("===> Choose A Vaild Option!")
        pygame.time.wait(1000)
        print("===> Returning Back To Menu")
        pygame.time.wait(500)
        Menu()


Menu()
