import pandas as pd
                      #avisando que é uma tabela
def create_example() -> pd.DataFrame:
    """_summary_ #resumo da função

    Returns:
        pd.DataFrame: _description_ #explicando
        #obs: tudo em inglês










        
    """

    tabela=pd.DataFrame({
        'Nome': ['Renata', 'Anderson', 'Paulo'],
        'Nota1': [10, 5, 9],
        'Nota2' : [7, 3, 9]
    })

    return tabela