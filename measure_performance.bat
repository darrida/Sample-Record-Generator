python -m cProfile -o performance_report.dat generate_sample_audit_data.py
snakeviz performance_report.dat