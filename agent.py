import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def summarize_document(text: str) -> str:
    """Use Claude to summarize a document."""
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"请对以下文档进行总结，提取关键信息，并生成一份简洁的报告：\n\n{text}"
            }
        ]
    )
    return message.content[0].text

def extract_key_points(text: str) -> str:
    """Extract key points from a document."""
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"请从以下文档中提取关键要点，用列表形式呈现：\n\n{text}"
            }
        ]
    )
    return message.content[0].text

def generate_report(text: str) -> str:
    """Generate a structured report from document content."""
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2048,
        messages=[
            {
                "role": "user",
                "content": f"""请根据以下文档内容生成一份结构化报告，包含：
1. 执行摘要
2. 主要发现
3. 关键数据点
4. 建议与结论

文档内容：
{text}"""
            }
        ]
    )
    return message.content[0].text

def run_agent(document_text: str, task: str = "summarize"):
    """
    Main agent function that processes documents based on task type.
    
    Args:
        document_text: The document content to process
        task: One of 'summarize', 'extract', or 'report'
    """
    print(f"\n{'='*50}")
    print(f"Claude 文档智能助手 Agent")
    print(f"任务类型: {task}")
    print(f"{'='*50}\n")
    
    if task == "summarize":
        print("正在生成文档摘要...")
        result = summarize_document(document_text)
    elif task == "extract":
        print("正在提取关键要点...")
        result = extract_key_points(document_text)
    elif task == "report":
        print("正在生成结构化报告...")
        result = generate_report(document_text)
    else:
        result = "未知任务类型，请选择: summarize, extract, 或 report"
    
    print("处理结果：")
    print("-" * 40)
    print(result)
    print("-" * 40)
    return result

if __name__ == "__main__":
    # 示例文档
    sample_document = """
    2024年第三季度业务报告
    
    本季度公司营收达到1.2亿元，同比增长35%。主要增长来源于：
    1. 新产品线贡献了40%的收入增长
    2. 海外市场拓展带来25%的新增客户
    3. 现有客户复购率提升至85%
    
    运营成本控制良好，净利润率维持在18%水平。
    研发投入占比达到营收的12%，重点在AI技术集成方面。
    
    下季度预期：营收增长目标设定为20%，将重点拓展东南亚市场。
    """
    
    # 运行Agent进行文档摘要
    run_agent(sample_document, task="summarize")
    
    # 运行Agent提取关键要点
    run_agent(sample_document, task="extract")
