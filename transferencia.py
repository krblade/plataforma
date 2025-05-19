import sqlite3

# Caminhos para os bancos de dados
caminho_banco_cheio = 'C:/Users/D1GQ/Downloads/banco/db.sqlite3'
caminho_banco_vazio = 'C:/Users\D1GQ/OneDrive - PETROBRAS/Desktop/PROJETOS/PLATAFORMA/plataforma/db.sqlite3'

# Conectar ao banco de dados vazio
conn_destino = sqlite3.connect(caminho_banco_vazio)
cur_destino = conn_destino.cursor()

# Anexar o banco de dados cheio
cur_destino.execute(f"ATTACH DATABASE '{caminho_banco_cheio}' AS origem;")

# Transferir os dados


cur_destino.execute("""
    INSERT INTO lotes_lote (Codigo,
                            Al,
                            Ano,
                            LocalArmazenamento,
                            IsaSipa,
                            DataSipa, 
                            TipoVenda, 
                            TipoMaterial,
                            IsaEnvioArm, 
                            DataEnvioArm, 
                            DataRecebimentoLote, 
                            PrazoEntrega, 
                            DataEntrega, 
                            PrazoConciliação,
                            DataConciliação, 
                            DataUltimaBaixa,
                            PrazodeBaixa,
                            DataPagamento,
                            PrazoPagamento, 
                            DataCancelamento,
                            Cancelado,
                            Prioridade,
                            Status,
                            DataMedicao,
                            PrazoMedicao,
                            PrazoConciliacaoCancelado,
                            DataConciliacaoCancelado,
                            DataAuditoria,
                            DataNegociacao,
                            EmNegociacao,
                            DataPagamentoLoteEx,
                            WriteDownStatus,
                            StatusDeEntrega,
                            PrazoEntregaAdicional, 
                            PrazoPagamentoAdicional, 
                            DataCadastroUltimaNota,
                            DataSolicitacaoConciliacao, 
                            DataSolicitacaoConciliacaoCancelado, 
                            Perdeuprazoentrega, 
                            MotivoPercaPrazo, 
                            Notificacao )
                     
    SELECT lote_lote,
            lote_al,
            lote_ano,
            lote_localArmazenamento,
            lote_isaSipa,
            lote_dataSipa,
            lote_tipoVenda,
            lote_tipoLote,
            lote_isaEnvioArm,
            lote_dataEnvoArm,
            lote_dataRecebimentoLote,
            lote_prazoEntrega,
            lote_dataEntrega,
            lote_prazoConciliação,
            lote_dataConciliação,
            lote_dataUltimaBaixaLote,
            lote_prazodeBaixa,
            lote_dataPagamentoLote,
            lote_prazoPagamentoLote,
            lote_dataCancelamento,
            lote_Cancelado,
            lote_Prioridade,
            lote_Status,
            lote_dataMedicao,
            lote_prazoMedicao,
            lote_prazoConciliacaoCAncelado,
            lote_dataConciliacaoCancelado,
            lote_dataAuditoria,
            lote_dataNegociacao,
            lote_emNegociacao,
            lote_dataPagamentoLoteEx,
            lote_WriteDownStatus,
            lote_statusDeEntrega,
            lote_prazoEntregaAdicional,
            lote_prazoPagamentoAdicional,
            lote_dataCadastroUltimaNota,
            lote_dataSolicitacaoConciliacao,
            lote_dataSolicitacaoConciliacaoCancelado,
            lote_perdeuprazoentrega,
            lote_motivopercaprazo, 
            lote_notificacao 

                    

    FROM origem.registros_lote;
""")

# Salvar (commit) as mudanças
conn_destino.commit()

# Desanexar o banco de dados origem
cur_destino.execute("DETACH DATABASE origem;")

# Fechar a conexão
cur_destino.close()
conn_destino.close()

print("Transferência de dados concluída com sucesso!")