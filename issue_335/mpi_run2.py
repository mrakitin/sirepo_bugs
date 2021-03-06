

from mpi4py import MPI
if MPI.COMM_WORLD.Get_rank():
    import signal
    signal.signal(signal.SIGTERM, lambda x, y: MPI.COMM_WORLD.Abort(1))

#!/usr/bin/env python
try:
    __IPYTHON__
    import sys
    del sys.argv[1:]
except:
    pass


import srwl_bl
import srwlib
import srwlpy


def set_optics(v=None):
    el = []
    el.append(srwlib.SRWLOptD(1e-16))

    el.append(srwlib.SRWLOptD(6.866))

    ifnMirror1 = ''  # "mirror_1d.dat"
    if ifnMirror1:
        hProfDataMirror1 = srwlib.srwl_uti_read_data_cols(ifnMirror1, "\t", 0, 1)
        el.append(srwlib.srwl_opt_setup_surf_height_1d(hProfDataMirror1, _dim="x", _ang=0.0436332, _amp_coef=1.0, _size_x=0.001, _size_y=0.001))
    el.append(srwlib.SRWLOptD(20.634))
    el.append(srwlib.SRWLOptG(_mirSub=srwlib.SRWLOptMirPl(_size_tang=0.2, _size_sag=0.015, _nvx=0.0, _nvy=0.99991607766, _nvz=-0.0129552165771, _tvx=0.0, _tvy=0.0129552165771), _m=1.0, _grDen=1800.0, _grDen1=0.08997, _grDen2=3.004e-06, _grDen3=9.73e-11, _grDen4=0.0))
    el.append(srwlib.SRWLOptA("r", "a", 0.015, 0.00259104331543, 0.0, 0.0))
    el.append(srwlib.SRWLOptD(34.63))
    el.append(srwlib.SRWLOptA("r", "a", 0.01832012956, 0.02, 0.0, 0.0))
    el.append(srwlib.SRWLOptMirEl(_p=89.63, _q=8.006, _ang_graz=0.0436332, _size_tang=0.42, _size_sag=0.02, _nvx=0.999048222947, _nvy=0.0, _nvz=-0.0436193560953, _tvx=-0.0436193560953, _tvy=0.0))
    el.append(srwlib.SRWLOptD(8.006))
    el.append(srwlib.SRWLOptA("r", "a", 0.0015, 0.0015, 0.0, 0.0))
    el.append(srwlib.SRWLOptD(6.01))
    el.append(srwlib.SRWLOptA("r", "a", 0.0130858068286, 0.003, 0.0, 0.0))
    el.append(srwlib.SRWLOptMirEl(_p=6.01, _q=0.911, _ang_graz=0.0872665, _size_tang=0.3, _size_sag=0.05, _nvx=0.996194694832, _nvy=0.0, _nvz=-0.0871557800056, _tvx=-0.0871557800056, _tvy=0.0))
    el.append(srwlib.SRWLOptD(0.5))
    el.append(srwlib.SRWLOptMirEl(_p=6.51, _q=0.411, _ang_graz=0.0872665, _size_tang=0.3, _size_sag=0.05, _nvx=0.0, _nvy=0.996194694832, _nvz=-0.0871557800056, _tvx=0.0, _tvy=-0.0871557800056))
    el.append(srwlib.SRWLOptD(0.411))

    pp = []
    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0])
    if ifnMirror1:
        pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 1.2, 3.5, 1.2, 3.0])
    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0])
    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 3.0, 1.0, 3.0, 1.0])
    pp.append([0, 0, 1.0, 0, 0, 0.4, 1.0, 0.4, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0])
    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 2.0, 1.0, 2.0, 1.0])
    pp.append([0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0])

    pp.append([0, 0, 1.0, 0, 1, 0.07, 1.5, 0.07, 6.0])

    return srwlib.SRWLOptC(el, pp)


varParam = srwl_bl.srwl_uti_ext_options([
    ['name', 's', 'NSLS-II ESM beamline tabulated undulator', 'simulation name'],

#---Data Folder
    ['fdir', 's', '', 'folder (directory) name for reading-in input and saving output data files'],

#---Electron Beam
    ['ebm_nm', 's', 'NSLS-II Low Beta Day 1', 'standard electron beam name'],
    ['ebm_nms', 's', '', 'standard electron beam name suffix: e.g. can be Day1, Final'],
    ['ebm_i', 'f', 0.5, 'electron beam current [A]'],
    ['ebm_de', 'f', 0.0, 'electron beam average energy deviation [GeV]'],
    ['ebm_x', 'f', 0.0, 'electron beam initial average horizontal position [m]'],
    ['ebm_y', 'f', 0.0, 'electron beam initial average vertical position [m]'],
    ['ebm_z', 'f', 0., 'electron beam initial average longitudinal position [m]'],
    ['ebm_dr', 'f', 0.0, 'electron beam longitudinal drift [m] to be performed before a required calculation'],
    ['ebm_ens', 'f', -1, ''],
    ['ebm_emx', 'f', -1, ''],
    ['ebm_emy', 'f', -1, ''],
    ['ebm_xp', 'f', 0, ''],
    ['ebm_yp', 'f', 0, ''],

#---Undulator
    ['und_bx', 'f', 0.0, 'undulator horizontal peak magnetic field [T]'],
    ['und_by', 'f', 0.8, 'undulator vertical peak magnetic field [T]'],
    ['und_phx', 'f', 0.0, 'initial phase of the horizontal magnetic field [rad]'],
    ['und_phy', 'f', 0.0, 'initial phase of the vertical magnetic field [rad]'],
    ['und_b2e', '', '', 'estimate undulator fundamental photon energy (in [eV]) for the amplitude of sinusoidal magnetic field defined by und_b or und_bx, und_by', 'store_true'],
    ['und_e2b', '', '', 'estimate undulator field amplitude (in [T]) for the photon energy defined by w_e', 'store_true'],
    ['und_per', 'f', 0.021, 'undulator period [m]'],
    ['und_len', 'f', 2.371, 'undulator length [m]'],
    ['und_zc', 'f', -1.5, 'undulator center longitudinal position [m]'],
    ['und_sx', 'i', 1, 'undulator horizontal magnetic field symmetry vs longitudinal position'],
    ['und_sy', 'i', -1, 'undulator vertical magnetic field symmetry vs longitudinal position'],
    ['und_g', 'f', 35.0, 'undulator gap [mm] (assumes availability of magnetic measurement or simulation data)'],
    ['und_ph', 'f', 0.0, 'shift of magnet arrays [mm] for which the field should be set up'],
    ['und_mdir', 's', 'magn_meas', 'name of magnetic measurements sub-folder'],
    ['und_mfs', 's', 'epu57_esm_sum_phase0.txt', 'name of magnetic measurements for different gaps summary file'],


#---Calculation Types
    # Electron Trajectory
    ['tr', '', '', 'calculate electron trajectory', 'store_true'],
    ['tr_cti', 'f', 0.0, 'initial time moment (c*t) for electron trajectory calculation [m]'],
    ['tr_ctf', 'f', 0.0, 'final time moment (c*t) for electron trajectory calculation [m]'],
    ['tr_np', 'f', 10000, 'number of points for trajectory calculation'],
    ['tr_mag', 'i', 2, 'magnetic field to be used for trajectory calculation: 1- approximate, 2- accurate'],
    ['tr_fn', 's', 'res_trj.dat', 'file name for saving calculated trajectory data'],
    ['tr_pl', 's', '', 'plot the resulting trajectiry in graph(s): ""- dont plot, otherwise the string should list the trajectory components to plot'],

    #Single-Electron Spectrum vs Photon Energy
    ['ss', '', '', 'calculate single-e spectrum vs photon energy', 'store_true'],
    ['ss_ei', 'f', 10.0, 'initial photon energy [eV] for single-e spectrum vs photon energy calculation'],
    ['ss_ef', 'f', 2000.0, 'final photon energy [eV] for single-e spectrum vs photon energy calculation'],
    ['ss_ne', 'i', 1000, 'number of points vs photon energy for single-e spectrum vs photon energy calculation'],
    ['ss_x', 'f', 0.0, 'horizontal position [m] for single-e spectrum vs photon energy calculation'],
    ['ss_y', 'f', 0.0, 'vertical position [m] for single-e spectrum vs photon energy calculation'],
    ['ss_meth', 'i', 1, 'method to use for single-e spectrum vs photon energy calculation: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler"'],
    ['ss_prec', 'f', 0.01, 'relative precision for single-e spectrum vs photon energy calculation (nominal value is 0.01)'],
    ['ss_pol', 'i', 6, 'polarization component to extract after spectrum vs photon energy calculation: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['ss_mag', 'i', 2, 'magnetic field to be used for single-e spectrum vs photon energy calculation: 1- approximate, 2- accurate'],
    ['ss_ft', 's', 'f', 'presentation/domain: "f"- frequency (photon energy), "t"- time'],
    ['ss_u', 'i', 1, 'electric field units: 0- arbitrary, 1- sqrt(Phot/s/0.1%bw/mm^2), 2- sqrt(J/eV/mm^2) or sqrt(W/mm^2), depending on representation (freq. or time)'],
    ['ss_fn', 's', 'res_spec_se.dat', 'file name for saving calculated single-e spectrum vs photon energy'],
    ['ss_pl', 's', '', 'plot the resulting single-e spectrum in a graph: ""- dont plot, "e"- show plot vs photon energy'],

    #Multi-Electron Spectrum vs Photon Energy (taking into account e-beam emittance, energy spread and collection aperture size)
    ['sm', '', '1', 'calculate multi-e spectrum vs photon energy', 'store_true'],
    ['sm_ei', 'f', 10.0, 'initial photon energy [eV] for multi-e spectrum vs photon energy calculation'],
    ['sm_ef', 'f', 1200.0, 'final photon energy [eV] for multi-e spectrum vs photon energy calculation'],
    ['sm_ne', 'i', 400, 'number of points vs photon energy for multi-e spectrum vs photon energy calculation'],
    ['sm_x', 'f', 0.0, 'horizontal center position [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_rx', 'f', 0.012, 'range of horizontal position / horizontal aperture size [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_nx', 'i', 1, 'number of points vs horizontal position for multi-e spectrum vs photon energy calculation'],
    ['sm_y', 'f', 0.0, 'vertical center position [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_ry', 'f', 0.012, 'range of vertical position / vertical aperture size [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_ny', 'i', 1, 'number of points vs vertical position for multi-e spectrum vs photon energy calculation'],
    ['sm_mag', 'i', 2, 'magnetic field to be used for calculation of multi-e spectrum spectrum or intensity distribution: 1- approximate, 2- accurate'],
    ['sm_hi', 'i', 1, 'initial UR spectral harmonic to be taken into account for multi-e spectrum vs photon energy calculation'],
    ['sm_hf', 'i', 15, 'final UR spectral harmonic to be taken into account for multi-e spectrum vs photon energy calculation'],
    ['sm_prl', 'f', 1.0, 'longitudinal integration precision parameter for multi-e spectrum vs photon energy calculation'],
    ['sm_pra', 'f', 1.0, 'azimuthal integration precision parameter for multi-e spectrum vs photon energy calculation'],
    ['sm_meth', 'i', 1, 'method to use for spectrum vs photon energy calculation in case of arbitrary input magnetic field: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler", -1- dont use this accurate integration method (rather use approximate if possible)'],
    ['sm_prec', 'f', 0.01, 'relative precision for spectrum vs photon energy calculation in case of arbitrary input magnetic field (nominal value is 0.01)'],
    ['sm_nm', 'i', 100, 'number of macro-electrons for calculation of spectrum in case of arbitrary input magnetic field'],
    ['sm_na', 'i', 5, 'number of macro-electrons to average on each node at parallel (MPI-based) calculation of spectrum in case of arbitrary input magnetic field'],
    ['sm_ns', 'i', 5, 'saving periodicity (in terms of macro-electrons) for intermediate intensity at calculation of multi-electron spectrum in case of arbitrary input magnetic field'],
    ['sm_type', 'i', 1, 'calculate flux (=1) or flux per unit surface (=2)'],
    ['sm_pol', 'i', 6, 'polarization component to extract after calculation of multi-e flux or intensity: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['sm_rm', 'i', 1, 'method for generation of pseudo-random numbers for e-beam phase-space integration: 1- standard pseudo-random number generator, 2- Halton sequences, 3- LPtau sequences (to be implemented)'],
    ['sm_fn', 's', 'res_spec_me.dat', 'file name for saving calculated milti-e spectrum vs photon energy'],
    ['sm_pl', 's', '', 'plot the resulting spectrum-e spectrum in a graph: ""- dont plot, "e"- show plot vs photon energy'],
    #to add options for the multi-e calculation from "accurate" magnetic field

    #Power Density Distribution vs horizontal and vertical position
    ['pw', '', '', 'calculate SR power density distribution', 'store_true'],
    ['pw_x', 'f', 0.0, 'central horizontal position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_rx', 'f', 0.015, 'range of horizontal position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_nx', 'i', 100, 'number of points vs horizontal position for calculation of power density distribution'],
    ['pw_y', 'f', 0.0, 'central vertical position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_ry', 'f', 0.015, 'range of vertical position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_ny', 'i', 100, 'number of points vs vertical position for calculation of power density distribution'],
    ['pw_pr', 'f', 1.0, 'precision factor for calculation of power density distribution'],
    ['pw_meth', 'i', 1, 'power density computation method (1- "near field", 2- "far field")'],
    ['pw_zst', 'f', 0., 'initial longitudinal position along electron trajectory of power density distribution (effective if pow_sst < pow_sfi)'],
    ['pw_zfi', 'f', 0., 'final longitudinal position along electron trajectory of power density distribution (effective if pow_sst < pow_sfi)'],
    ['pw_mag', 'i', 1, 'magnetic field to be used for power density calculation: 1- approximate, 2- accurate'],
    ['pw_fn', 's', 'res_pow.dat', 'file name for saving calculated power density distribution'],
    ['pw_pl', 's', '', 'plot the resulting power density distribution in a graph: ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],

    #Single-Electron Intensity distribution vs horizontal and vertical position
    ['si', '', '', 'calculate single-e intensity distribution (without wavefront propagation through a beamline) vs horizontal and vertical position', 'store_true'],
    #Single-Electron Wavefront Propagation
    ['ws', '', '', 'calculate single-electron (/ fully coherent) wavefront propagation', 'store_true'],
    #Multi-Electron (partially-coherent) Wavefront Propagation
    ['wm', '', '', 'calculate multi-electron (/ partially coherent) wavefront propagation', 'store_true'],

    ['w_e', 'f', 695.5, 'photon energy [eV] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ef', 'f', -1., 'final photon energy [eV] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ne', 'i', 1, 'number of points vs photon energy for calculation of intensity distribution'],
    ['w_x', 'f', 0.0, 'central horizontal position [m] for calculation of intensity distribution'],
    ['w_rx', 'f', 0.01, 'range of horizontal position [m] for calculation of intensity distribution'],
    ['w_nx', 'i', 100, 'number of points vs horizontal position for calculation of intensity distribution'],
    ['w_y', 'f', 0.0, 'central vertical position [m] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ry', 'f', 0.01, 'range of vertical position [m] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ny', 'i', 100, 'number of points vs vertical position for calculation of intensity distribution'],
    ['w_smpf', 'f', 0.08, 'sampling factor for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_meth', 'i', 1, 'method to use for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_prec', 'f', 0.01, 'relative precision for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_u', 'i', 1, 'electric field units: 0- arbitrary, 1- sqrt(Phot/s/0.1%bw/mm^2), 2- sqrt(J/eV/mm^2) or sqrt(W/mm^2), depending on representation (freq. or time)'],
    ['si_pol', 'i', 6, 'polarization component to extract after calculation of intensity distribution: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['si_type', 'i', 0, 'type of a characteristic to be extracted after calculation of intensity distribution: 0- Single-Electron Intensity, 1- Multi-Electron Intensity, 2- Single-Electron Flux, 3- Multi-Electron Flux, 4- Single-Electron Radiation Phase, 5- Re(E): Real part of Single-Electron Electric Field, 6- Im(E): Imaginary part of Single-Electron Electric Field, 7- Single-Electron Intensity, integrated over Time or Photon Energy'],
    ['w_mag', 'i', 2, 'magnetic field to be used for calculation of intensity distribution vs horizontal and vertical position: 1- approximate, 2- accurate'],

    ['si_fn', 's', 'res_int_se.dat', 'file name for saving calculated single-e intensity distribution (without wavefront propagation through a beamline) vs horizontal and vertical position'],
    ['si_pl', 's', '', 'plot the input intensity distributions in graph(s): ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],
    ['ws_fni', 's', 'res_int_pr_se.dat', 'file name for saving propagated single-e intensity distribution vs horizontal and vertical position'],
    ['ws_pl', 's', '', 'plot the resulting intensity distributions in graph(s): ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],

    ['wm_nm', 'i', 100000, 'number of macro-electrons (coherent wavefronts) for calculation of multi-electron wavefront propagation'],
    ['wm_na', 'i', 5, 'number of macro-electrons (coherent wavefronts) to average on each node for parallel (MPI-based) calculation of multi-electron wavefront propagation'],
    ['wm_ns', 'i', 5, 'saving periodicity (in terms of macro-electrons / coherent wavefronts) for intermediate intensity at multi-electron wavefront propagation calculation'],
    ['wm_ch', 'i', 0, 'type of a characteristic to be extracted after calculation of multi-electron wavefront propagation: #0- intensity (s0); 1- four Stokes components; 2- mutual intensity cut vs x; 3- mutual intensity cut vs y'],
    ['wm_ap', 'i', 0, 'switch specifying representation of the resulting Stokes parameters: coordinate (0) or angular (1)'],
    ['wm_x0', 'f', 0, 'horizontal center position for mutual intensity cut calculation'],
    ['wm_y0', 'f', 0, 'vertical center position for mutual intensity cut calculation'],
    ['wm_ei', 'i', 0, 'integration over photon energy is required (1) or not (0); if the integration is required, the limits are taken from w_e, w_ef'],
    ['wm_rm', 'i', 1, 'method for generation of pseudo-random numbers for e-beam phase-space integration: 1- standard pseudo-random number generator, 2- Halton sequences, 3- LPtau sequences (to be implemented)'],
    ['wm_fni', 's', 'res_int_pr_me.dat', 'file name for saving propagated multi-e intensity distribution vs horizontal and vertical position'],

    #to add options
    ['op_r', 'f', 30.0, 'longitudinal position of the first optical element [m]'],

    # Former appParam:
    ['source_type', 's', 't', 'source type, (u) idealized undulator, (t), tabulated undulator, (m) multipole, (g) gaussian beam'],

#---User Defined Electron Beam
    ['ueb', 'i', 0, 'Use user defined beam'],
    ['ueb_e', 'f', 3.0, 'energy [GeV]'],
    ['ueb_sig_e', 'f', 0.00089, 'RMS energy spread'],
    ['ueb_beam_definition', 's', 't', 'definition of the beam using Twiss Parameters (t) or Moments (m)'],
    ['ueb_emit_x', 'f', 9e-10, 'horizontal emittance [m]'],
    ['ueb_beta_x', 'f', 2.02, 'horizontal beta-function [m]'],
    ['ueb_alpha_x', 'f', 0.0, 'horizontal alpha-function [rad]'],
    ['ueb_eta_x', 'f', 0.0, 'horizontal dispersion function [m]'],
    ['ueb_eta_x_pr', 'f', 0.0, 'horizontal dispersion function derivative [rad]'],
    ['ueb_emit_y', 'f', 8e-12, 'vertical emittance [m]'],
    ['ueb_beta_y', 'f', 1.06, 'vertical beta-function [m]'],
    ['ueb_alpha_y', 'f', 0.0, 'vertical alpha-function [rad]'],
    ['ueb_eta_y', 'f', 0.0, 'vertical dispersion function [m]'],
    ['ueb_eta_y_pr', 'f', 0.0, 'vertical dispersion function derivative [rad]'],
    ['ueb_rms_size_x', 'f', 4.26380112107e-05, "horizontal RMS size [m]"],
    ['ueb_rms_diverg_x', 'f', 2.11079263419e-05, "horizontal RMS divergence [rad]"],
    ['ueb_xxpr_x', 'f', 0.0, "horizontal <(x-<x>)(x'-<x'>)> [m]"],
    ['ueb_rms_size_y', 'f', 2.91204395571e-06, "vertical RMS size [m]"],
    ['ueb_rms_diverg_y', 'f', 2.74721127897e-06, "vertical RMS divergence [rad]"],
    ['ueb_xxpr_y', 'f', 0.0, "vertical <(x-<x>)(x'-<x'>)> [m]"],
])

import srwl_bl
v = srwl_bl.srwl_uti_parse_options(varParam, use_sys_argv=True)
source_type, mag = srwl_bl.setup_source(v)
v.wm_na = v.sm_na = 5
# Number of "iterations" per save is best set to num processes
v.wm_ns = v.sm_ns = 2
op = set_optics()
srwl_bl.SRWLBeamline(_name=v.name).calc_all(v, op)
