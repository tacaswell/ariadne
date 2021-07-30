from bluesky_widgets.models.auto_plot_builders import AutoPlotter
from bluesky_widgets.models.plot_builders import Lines
from bluesky_widgets.models.plot_specs import Axes, Figure

class AutoBMMPlot(AutoPlotter):

    def handle_new_stream(self, run, stream_name):
        if stream_name == 'primary':
            plan_name = run.metadata['start'].get('plan_name').replace(' ', '_')
            # Check if plotting has been configured for this plan_name.
            # If there is no plotting configured, do nothing.
            if hasattr(self, plan_name):
                models, figures = getattr(self, plan_name)(run, stream_name)
                for model in models:
                    model.add_run(run)
                    self.plot_builders.append(model)
                self.figures.extend(figures)

    def rel_scan_linescan_xafs_y_it(self, run, stream_name):
        # FIXME: Need to sort out how to get the correct motor here
        x_values = 'xafs_y'
        models = []
        figures = []

        axes1 = Axes()
        figure1 = Figure((axes1,), title="It_divided_by_I0")
        figures.append(figure1)
        models.append(
            Lines(x=x_values, ys=['It/I0',], max_runs=1, axes=axes1)
        )

        axes2 = Axes()
        figure2 = Figure((axes2,), title="I0")
        figures.append(figure2)
        models.append(
            Lines(x=x_values, ys=['I0',],    max_runs=1, axes=axes2)
        )

        return models, figures

    def rel_scan_linescan_xafs_pitch_it(self, run, stream_name):
        x_values = run.metadata['start']['motors'][0]
        models = []
        figures = []

        axes = Axes()
        figure = Figure((axes,), title="I0")
        figures.append(figure)
        models.append(
            Lines(x=x_values, ys=['I0',],    max_runs=1, axes=axes)
        )

        return models, figures

    def rel_scan_linescane_xafs_y_if(self, run, stream_name):
        x_values = run.metadata['start']['motors'][0]
        models = []
        figures = []

        axes = Axes()
        figure = Figure((axes,), title="I0")
        figures.append(figure)
        models.append(
            Lines(x=x_values, ys=['I0',],    max_runs=1, axes=axes)
        )

        return models, figures

    def scan_nd_xafs_trans(self, run, stream_name):
        x_values = run.metadata['start']['motors'][0]
        models = []
        figures = []

        axes1 = Axes()
        axes2 = Axes()
        figure = Figure((axes1, axes2), title='It and I0')
        figures.append(figure)
        models.append(
            Lines(x=x_values, ys=['It/I0',], max_runs=1, axes=axes1)
        )
        models.append(
            Lines(x=x_values, ys=['I0',],    max_runs=1, axes=axes2)
        )

        return models, figures

    def scan_nd_xafs_fluorescence(self, run, stream_name):
        x_values = run.metadata['start']['motors'][0]
        models = []
        figures = []

        axes1 = Axes()
        axes2 = Axes()
        figure = Figure((axes1, axes2), title='It and I0')
        figures.append(figure)
        models.append(
            Lines(x=x_values, ys=['It/I0',], max_runs=1, axes=axes1)
        )
        models.append(
            Lines(x=x_values, ys=['I0',],    max_runs=1, axes=axes2)
        )

        return models, figures
