from __future__ import print_function
import subprocess

dfes = [('simulated', '2mb', 0.5, 10, 0.25, 50), ('predicted', '2mb', 0.51, 144.7, 0.253, 93.2),
        ('simulated', '20mb', 0.5, 10, 0.25, 50), ('predicted', '20mb', 0.51, 10.4, 0.251, 51.2)]

print('cat', 'prop', 'var', 'data_type', 'seq_len', sep='\t')
          
for dfe in dfes:

  gamma_cmd = '~/parus_indel/anavar_analyses/gen_gamma_plot_data.py -sh_i {} -sc_i {} -sh_d {} -sc_d {} '.format(*dfe[2:])
  gamma_data = subprocess.Popen(gamma_cmd, shell=True, stdout=subprocess.PIPE).communicate()[0].split('\n')[1:-1]
  
  for line in gamma_data:
    new_line = '{}\t{}\t{}'.format(line, dfe[0], dfe[1])
    print(new_line)
