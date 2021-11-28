from sklearn.base import BaseEstimator, TransformerMixin


# Um transformador para limpar o dataframe
class Clean(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        
        # Tranformamos os valores em string para float
        data.EXISTING_SAVINGS = pd.to_numeric(data['EXISTING_SAVINGS'], errors='coerce')
        data.CHECKING_BALANCE = pd.to_numeric(data['CHECKING_BALANCE'], errors='coerce')

        categorical_columns = [
            'INSTALLMENT_PLANS',
            'LOAN_PURPOSE',
            'OTHERS_ON_LOAN',
            'SEX',
            'PROPERTY',
            'HOUSING',
            'CREDIT_HISTORY',
        ]

        # One hote encoding
        for column in categorical_columns:
            hot_encoded = pd.get_dummies(df[column])
            data = pd.concat((data, hot_encoded), axis=1)

        # Removendo as colunas categóricas
        data = data.drop(categorical_columns, axis=1,errors='ignore')
        data = data.drop('NONE', axis=1, errors='ignore')

        # Removendo a coluna target
        data = data.drop('ALLOW', axis=1, errors='ignore')
        
        return data