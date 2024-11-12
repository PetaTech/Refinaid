from typing import Any

import gradio as gr


def build_tw_stock_calculator() -> gr.Blocks:

    demo = gr.Blocks(
        title='Trade Tracker ™️',
    )

    with demo:
        gr.HTML(
            "<h1 align=center>Trade Tracker ™️</h1>"
        )

        calculator_tab = init_calculator()
        reverse_tab = init_reserve()


    return demo


def init_reserve():

    with gr.Tab("Reverse") as reserve_tab:

        gr.Markdown(
            "# Reverse Tab",)
        
    return reserve_tab


def init_calculator():
    with gr.Tab("台股計算機") as calculator_tab:

        with gr.Row():
            with gr.Column(scale=1):

                broker = gr.Dropdown(
                    label="Please select a broker",
                    info="Select a broker",
                    value="Fubon",
                    choices=["Fubon"],
                    interactive=True,
                    multiselect=None,
                )
                broker_info = gr.Markdown(
                    f"""\
                    - 手續費: 0.1425%
                    - 一般手續費折扣: N/A
                    - 證券交易稅: 0.3%

                    (如有其他手續費，可自行輸入)
                    """,
                )
            with gr.Column(scale=2):

                with gr.Row():
                    with gr.Column(scale=2):
                        stock = gr.Number(
                            label="股 (stock)",
                            value=1000,
                            interactive=True,
                        )
                        amount = gr.Number(
                            label="單量 (amount)",
                            value=1,
                            interactive=True,
                        )
                    with gr.Column(scale=1):
                        stock_id = gr.Textbox(
                            label="股票代號 (optional)",
                            value="2330",
                            interactive=True,
                        )

                with gr.Row():
                    purchase_price = gr.Number(
                        label="買入價格",
                        step=0.01,
                    )

                    sell_price = gr.Number(
                        label="賣出價格",
                        step=0.01,
                    )

        with gr.Row():
            with gr.Column(scale=1):
                with gr.Row():
                    gr.Checkbox(
                        label="當沖", 
                        info=""
                    )
                    amount = gr.Number(
                        label="$",
                        value=1,
                        interactive=True,
                    )
                with gr.Row():
                    gr.Checkbox(
                        label="ETF", 
                        info=""
                    )
                    amount = gr.Number(
                        label="$",
                        value=1,
                        interactive=True,
                    )
            with gr.Column(scale=2):
                amount = gr.Number(
                    label="手續費",
                    value=1,
                    interactive=True,
                )
                amount = gr.Number(
                    label="手續費折扣",
                    value=1,
                    interactive=True,
                )
    return calculator_tab

def main():
    build_tw_stock_calculator().launch()

if __name__ == "__main__":
    main()
