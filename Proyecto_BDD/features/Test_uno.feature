Feature: Nuestro primer Demo

  Background:
    Given Abriendo el navegador

  Scenario Outline: Corriendo nuestro primer test

      When Cargando el nombre del "<nombre>"
      Then Cargando su "<email>".
      Then Cargando la "<direccion>"
      Examples:
      | nombre | email | direccion |
      | nombre1 | email1@gmail.com | direccion1 |
      | nombre2 | email2@gmail.com | direccion2 |
      | nombre3 | email3@gmail.com | direccion3 |
      | nombre4 | email4@gmail.com | direccion4 |

  #Scenario: Corriendo nuestro segundo test

   #   When Cargando el nombre del "Marisol"
    #  Then Cargando su "marisol@gmail.com".
     # Then Cargando la "Direccion dos"