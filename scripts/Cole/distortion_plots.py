import os
import pandas as pd
import plotly.io as pio

from hallprobecalib.hpcplots import histo

datadir = '/home/ckampa/data/pickles/distortions/linear_gradient/'
plotdir = '/home/ckampa/data/plots/distortions/linear_gradient/'

for d in [plotdir, plotdir+'run_04/', plotdir+'run_04/LHelix_reco/']:
    if not os.path.exists(d):
        os.makedirs(d)

# dist_name = 'LinGrad'
dist_name = 'Mau10_0TS'
if dist_name == 'LinGrad':
    file_suffix = dist_name
else:
    file_suffix = 'LHelix'


df_run = pd.read_pickle(datadir+f'run_04/MC_sample_plus_reco_{file_suffix}.pkl')
# df_run = pd.read_pickle(datadir+'run_04/MC_sample_plus_reco_LHelix.pkl')
# df_run = pd.read_pickle(datadir+'run_04/MC_sample_plus_reco_LinGrad.pkl')
# df_run = pd.read_pickle(datadir+'run_04/MC_sample_plus_reco_chi2.pkl')
# df_run = pd.read_pickle(datadir+'run_04/MC_sample_plus_reco.pkl')
# df_run = pd.read_pickle(datadir+'run_01/MC_sample_plus_reco.pkl')
# df_run2 = pd.read_pickle(datadir+'run_02-10x_grad/MC_sample_plus_reco.pkl')

df_run.loc[:, 'Residual Nominal'] = df_run['mom_LHelix_nom'] - df_run['p_mc']
df_run.loc[:, 'Residual Distorted'] = df_run['mom_LHelix_dis'] - df_run['p_mc']
# df_run.loc[:, 'Residual Nominal'] = df_run['p_chi2_nom'] - df_run['p_mc']
# df_run.loc[:, 'Residual Distorted'] = df_run['p_chi2_dis'] - df_run['p_mc']
# df_run.loc[:, r'Standard Deviation Reco p (Nominal)'] = df_run['p_chi2_nom'].std()
# df_run.loc[:, r'Standard Deviation Reco p (Distorted)'] = df_run['p_chi2_dis'].std()
# df_run.loc[:, 'Residual Nominal'] = df_run['p_nom'] - df_run['p_mc']
# df_run.loc[:, 'Residual Distorted'] = df_run['p_dis'] - df_run['p_mc']
# df_run.loc[:, r'Standard Deviation Reco p (Nominal)'] = df_run['std_p_nom']
# df_run.loc[:, r'Standard Deviation Reco p (Distorted)'] = df_run['std_p_dis']
# df_run2.loc[:, 'Residual Nominal'] = df_run2['p_nom'] - df_run2['p_mc']
# df_run2.loc[:, 'Residual Distorted'] = df_run2['p_dis'] - df_run2['p_mc']

N = 75
N2 = 200

plot_file_pre = plotdir+f'run_04/LHelix_reco/{dist_name}/'

fig = histo([df_run['Residual Nominal']], bins=N, inline=False, show_plot=False)
fig.update_layout(xaxis=dict(title=r"$\text{Residual }(p_{\text{reco}} - p_{\text{MC}}) [\text{MeV } c^{-1}]$"),title="Mau 13 (nominal)")
pio.write_image(fig, plot_file_pre+'hist_residuals_nom.pdf')
pio.write_image(fig, plot_file_pre+'hist_residuals_nom.png')

fig = histo([df_run['Residual Distorted']], bins=N, inline=False, show_plot=False)
fig.update_layout(xaxis=dict(title=r"$\text{Residual }(p_{\text{reco}} - p_{\text{MC}}) [\text{MeV } c^{-1}]$"),title=f"Distorted ({dist_name})")
pio.write_image(fig, plot_file_pre+'hist_residuals_dis.pdf')
pio.write_image(fig, plot_file_pre+'hist_residuals_dis.png')

fig = histo([df_run['Residual Nominal'], df_run['Residual Distorted']], bins=N2, same_bins=True, inline=False, show_plot=False)
fig.update_layout(xaxis=dict(title=r"$\text{Residual }(p_{\text{reco}} - p_{\text{MC}}) [\text{MeV } c^{-1}]$"),title=f"Distorted ({dist_name})")
pio.write_image(fig, plot_file_pre+'residual_mean_comparison.pdf')
pio.write_image(fig, plot_file_pre+'residual_mean_comparison.png')
# pio.write_image(fig, plotdir+'run_04/residual_mean_comparison_100_Gauss.pdf')
# pio.write_image(fig, plotdir+'run_04/residual_mean_comparison_100_Gauss.png')
# pio.write_image(fig, plotdir+'run_01/residual_comparison_100_Gauss.pdf')

# fig = histo([df_run['Standard Deviation Reco p (Nominal)'], df_run['Standard Deviation Reco p (Distorted)']], bins=N, inline=False, show_plot=False)
# fig.update_layout(xaxis=dict(title=r"$\text{Standard Deviation along trajectory } [\text{MeV } c^{-1}]$"),title="Linear Gradient: 100 Gauss to 0 Gauss")
# pio.write_image(fig, plotdir+'run_04/stddev_comparison_100_Gauss.pdf')

# fig = histo([df_run2['Residual Nominal'], df_run2['Residual Distorted']], bins=N, inline=False, show_plot=False)
# fig.update_layout(xaxis=dict(title=r"$\text{Residual }(p_{\text{reco}} - p_{\text{MC}}) [\text{MeV } c^{-1}]$"),title="Linear Gradient: 1000 Gauss to 0 Gauss")
# pio.write_image(fig, plotdir+'run_02-10x_grad/residual_comparison_1000_Gauss.pdf')
